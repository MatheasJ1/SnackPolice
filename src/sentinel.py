#!/usr/bin/env python3

import os
import sys
import subprocess
import time
from datetime import datetime
import requests
import base64



PROX_THRESHOLD = 7000
COOLDOWN_SECONDS = 5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTO_DIR = os.path.join(SCRIPT_DIR, "caught_photos")
VENV_DIR = os.path.join(SCRIPT_DIR, ".caughtya_env")
WEBCAM_DEVICE = "/dev/video0"

HA_URL = "http://10.0.0.235:8123"
WEBHOOK_UPLOAD = "caught_ya_upload"   



def in_venv() -> bool:
    return os.path.abspath(sys.prefix) == os.path.abspath(VENV_DIR)

def ensure_venv_and_deps():
    if in_venv():
        return

    if not os.path.isdir(VENV_DIR):
        print(f"[SETUP] Creating venv at {VENV_DIR}")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)

    python_venv = os.path.join(VENV_DIR, "bin", "python3")

    print("[SETUP] Upgrading pip...")
    subprocess.run([python_venv, "-m", "pip", "install", "--upgrade", "pip"], check=True)

    print("[SETUP] Installing deps...")
    subprocess.run([python_venv, "-m", "pip", "install", "adafruit-circuitpython-vcnl4010"], check=True)

    print("[SETUP] Restarting script inside venv...")
    os.execv(python_venv, [python_venv, os.path.abspath(__file__)] + sys.argv[1:])

if not in_venv():
    ensure_venv_and_deps()



import board
import busio
import adafruit_vcnl4010



os.makedirs(PHOTO_DIR, exist_ok=True)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4010.VCNL4010(i2c)

last_shot_time = 0


def upload_to_home_assistant(photo_path):
    """
    Uploads image via webhook using base64.
    This works on ALL Home Assistant installs (Core / Container / OS).
    """
    url = f"{HA_URL}/api/webhook/{WEBHOOK_UPLOAD}"

    with open(photo_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    payload = {"file": encoded}

    try:
        r = requests.post(url, json=payload)
        print("[UPLOAD]", r.status_code, r.text)
    except Exception as e:
        print("[ERROR] Upload failed:", e)

# =========================
# ALERT WEBHOOK (NOTIFICATION)
# =========================

def trigger_webhook():
    """Triggers your existing caught_ya_alert automation (phone notif)."""
    url = f"{HA_URL}/api/webhook/{WEBHOOK_ALERT}"
    try:
        r = requests.post(url)
        print("[WEBHOOK]", r.status_code)
    except Exception as e:
        print("[WEBHOOK ERROR]", e)

# =========================
# TAKE PICTURE
# =========================

def take_picture():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(PHOTO_DIR, f"caught_{timestamp}.jpg")

    cmd = [
        "fswebcam",
        "-d", WEBCAM_DEVICE,
        "-r", "1280x720",
        "--no-banner",
        filename,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"[INFO] Saved {filename}")
    except Exception as e:
        print("[ERROR] fswebcam failed", e)

    # also save a static version for Home Assistant
    latest = os.path.join(PHOTO_DIR, "latest.jpg")
    subprocess.run(["cp", filename, latest])
    return latest

# =========================
# MAIN LOOP
# =========================

def main():
    global last_shot_time
    print("Starting VCNL4010 motion watcher...")

    while True:
        prox = sensor.proximity
        print("Proximity:", prox)

        now = time.time()

        if prox > PROX_THRESHOLD and (now - last_shot_time) > COOLDOWN_SECONDS:
            print("!! THRESHOLD REACHED — TAKING PHOTO !!")
            latest_path = take_picture()

            upload_to_home_assistant(latest_path)  
            trigger_webhook()                      

            last_shot_time = now

        time.sleep(0.2)

if __name__ == "__main__":
    main()
