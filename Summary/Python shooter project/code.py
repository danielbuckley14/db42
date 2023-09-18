
from adafruit_circuitplayground import cp
#we import circuit python express. We will use cp to refer to boards sensors and lights
#we import our LightDisplay class from the lightdisplay file
from sensorlightdisplay import SensorLightDisplay
#we import the SensorLightDisplay class from the sensorlightdisplay
import time
#we import time so we can add delays to our programme
#we create an instance of the of the class and pass in the brightness to be used for the object
sensorlightdisplay_1 = SensorLightDisplay(.01)
#we do the same with the sensorlightdisplay class
colour = [0,0,255]

list_of_colours = [[202, 24, 78], [113, 91, 193], [208, 254, 232], [183, 235, 77], [243, 177, 240], [81, 175, 56], [232, 166, 206], [15, 192, 197], [243, 177, 240], [150, 216, 222]]
#we create the colour variables to pass into our methods
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices)

while True:
    x = cp.acceleration[0]
    #this stores the acceleration of the board on the x access
    y = cp.acceleration[1]
    acceleration_peak = 9.81
    if cp.switch:
        if cp.button_a:
            kbd.press(Keycode.SPACE)

        else:
            kbd.release(Keycode.SPACE)

        if x < 0:
            flipped_x = x * -1
        else:
            flipped_x = x
        if flipped_x <= acceleration_peak:
            # problem 1: if x < - 3, press left arrow
            if x < - 3:
                # kbd.send(Keycode.LEFT_ARROW) # used to press AND release a key on the keyboard
                kbd.press(Keycode.LEFT_ARROW) # used to press AND NOT RELEASE a key on the keyboard
                kbd.release(Keycode.C)
            elif x > 3:

                kbd.press(Keycode.RIGHT_ARROW)
                kbd.release(Keycode.LEFT_ARROW)
            else:
                kbd.release(Keycode.RIGHT_ARROW)
                kbd.release(Keycode.LEFT_ARROW)




    #sensorlightdisplay_1.half_light(x, colour)
    #sensorlightdisplay_1.control_feedback_y(y)
    #sensorlightdisplay_1.control_feedback_x(x)
    sensorlightdisplay_1.control_feedback(x, colour)
