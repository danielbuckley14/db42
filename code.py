
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
#we create the colour variable to pass into our methods


while True:

    x = cp.acceleration[0]
    #this stores the acceleration of the board on the x access
    y = cp.acceleration[1]


    #lightdisplay_1.half_pattern(colour)

    #lightdisplay_1.half_light(0, colour)

    #lightdisplay_1.random_light(colour, .5)

    #lightdisplay_1.snake(3, colour, 1)
    #sensorlightdisplay_1.half_light(x, colour)
    #sensorlightdisplay_1.control_feedback_y(y)
    sensorlightdisplay_1.control_feedback_x(x, colour)
