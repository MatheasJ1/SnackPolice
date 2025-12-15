
# INSTALLATION INSTRUCTIONS


Project: Snack Police
Chosen Setup: Raspberry Pi OS + Python + Home Assistant Integration


## 1. REQUIREMENTS

- Raspberry Pi with Raspberry Pi OS
- Python 3
- I2C enabled (raspi-config)
- Internet connection for Home Assistant integration
- VCNL4010 or any sensor that works best for inteded use
- A camera/webcam for taking the snapshots
- A breadboard
- Jumper wires



## 2. INSTALL DEPENDENCIES
Enable I2C on the PI:

    sudo raspi-config

Install required Python libraries:

    pip install adafruit-circuitpython-vcnl4010 RPLCD smbus2 requests

Install requires programs : python 3 + venv

    sudo apt update
    sudo apt install -y python3


    

OR use venv to get into an environment because python causes some issues
when installing some libraries. When inside the environment (will see venv next to ur name in terminal) you can then install and use the requested library.

### Venv

    sudo apt install -y python3-venv
Activate and check the venv 

    source (venvName)/bin/activate
    
Adafruit libraires for sensor prox (after youve created the virtual env.)

    pip install adafruit-circuitpython-vcnl4010


## 3. DOWNLOAD PROJECT FILES

### Clone or copy project files into a working directory:

    git clone https://github.com/MatheasJ1/SnackPolice.git


## 4. HOME ASSISTANT SETUP

### Install Home assistant ISO image : https://www.home-assistant.io/installation/windows 

### Install VirtualBox : https://www.virtualbox.org

### Create a Virtual Machine with the Home Assistant ISO (I personally used this vido to help me with the setup) : https://www.youtube.com/watch?v=JZUMYyp2US4
    
When inside your Home Assistant VM you can access the menu through a local browser and start setting up your account to your liking.

## 5. RUNNING THE SCRIPT

### Execute the main program:

    python3 SnackPolice.py (not completed yet)

This will:
- Create a VENV and ensure you're in it before continuing the script
- Then, it will initialize everything from hardware to directories
- Read proximity from the VCNL4010 sensor
- Display values on the terminal
- Trigger a "CAUGHT YA!" alert when threshold is exceeded
- Send webhook notifications to Home Assistant via the python web server URL for images


## 6. HOME ASSISTANT SETUP (MINIMAL)

### Create a webhook automation in Home Assistant and note the webhook URL.

The webhook ID should match the one that's in the script and you must configure your phone as an 'Entity' on Home Assisatnt so that you can use the feature to send it to your mobile phone, which of course, also needs to have Home Assistant already setup and connected to the same account.

### Set your URL inside the script:

    WEBHOOK_URL = "http://<ip>:8123/api/webhook/<webhook_id>"

## 7. HOW IT WORKS
- Whenever you feel like it, you can choose to run or stop the script.
- For the script to start at boot you can either use systemd or a cron job to operate that task everytime the machine boots up.
- It will read the prox and detect anyone that's been tampering with the drawer that's being watched by the detection system.


## 8. UNINSTALL

### Remove the project folder:

    rm -rf  SnackPolice
