# Snack Theft Detection System

This projects puts into use a Raspberry Pi, a VCNL4010 proximity sensor and a AverMedia webcam to capture anyone trying to steal snacks from a spefiic place.
The picture of the theif is taken and sent through a push notification using Home Assistant. The webcam then captures a picture and updates a Home assistant picture which is set to the latest captured picture in specified directory.

The system monitors a specific location and taes a snapshot when physical movement surpasses the set threshold of the sensor. This project demonstrates how automation and hardware can be conbined to create real world utilities.

The goal of this project is to combine linux tools, physical sensors, camera interaction, scripting and automation.


## Components

### Hardware 
- Raspberry PI
- Adafruit VCNL4010 proximity sensor
- USB webcam (Anything compatible with fswebcam)
- Breadboard
- Jumperwires
- LCD Display for funny messages(OPTIONAL)

### Software
- Raspberry PI OS
- fswebcam
- python3 +  web server + virtual environments
- I2C libraires
- Home assistant VM
- VCNL4010 packages

## Important features
- Real-time proximity detection
- Automated image capture + push
- Home assistant dashboard view
- Expandable and subjective to user's desires

## Improved skills
- Linux system administration
- Python scripting
- Virtual environments
- Wriring
- I2C communication
- debugging and troubleshooting systems


