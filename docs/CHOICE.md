# Two possible setups : 

 ## 1. Raspberry Pi OS + Python + Home assistant integration
Pros
- Full and easy access to I2C GPIO.
- Ideal for controling the hardaware.(sensors, lcd display and webcam)
- Easy control of sensors and webcams.
- Home Assist. Integration provides necessary tools.
- Allows for automation customization.


### Cons
  - Requires more setup than flashing Home Assistant OS
  - Require more initial setup ( packagesm libraries and home assistant)


## 2. Home Assistant OS (Flashed directly)
### Pros
- Simplified automation environment.
- Built in widgets and config settings.
- Very simple to install and maintain.
- Built-in tools for automation.
- Offers user-friendly interface.

### Cons
- Harder to run scripts, customize automation
- Limited access and configuration with GPIO and I2C
- Not suitable for sensor control

## Chosen Solution:

I chose **Raspberry Pi OS + Python + Home Assistant Integration** because it offers full hardware control while still making notifications, webcame automation and everything work great. It allows the project to capture sensor events, process them, take snapshots and send alerts. all of which would be way harder to access if I were to be using the Home Assistant OS. 

