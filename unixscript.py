import time
import board
import busio
from adafruit_vcnl4010 import VCNL4010
from RPLCD.i2c import CharLCD

i2c = busio.I2C(board.SCL, board.SDA)
sensor = VCNL4010(i2c)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)

while True:
    prox = sensor.proximity
    lcd.clear()
    if prox >= 7000:
        lcd.write_string("YOU GOT CAUGHT!")
    else:
        lcd.write_string(str(prox))
    time.sleep(0.2)
