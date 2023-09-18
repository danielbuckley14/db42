from adafruit_circuitplayground import cp
import time

class SensorLightDisplay:
    def __init__(self, brightness):
        self.colour_black = [0, 0, 0]
        self.number_of_neopixels = len(cp.pixels)
        cp.pixels.auto_write = False
        cp.pixels.brightness = brightness
    def advanced_control_feedback(self):
        pass


    def half_light(self, acceleration_x, colour):
        if acceleration_x < 9.81 and acceleration_x > -9.81 :
            if acceleration_x < 3:
                for pixel in range(5, self.number_of_neopixels):
                    cp.pixels[pixel] = colour
                for pixel in range(0, self.number_of_neopixels-5):
                    cp.pixels[pixel] = self.colour_black

            elif acceleration_x > 3:
                for pixel in range(0, self.number_of_neopixels-5):
                    cp.pixels[pixel] = colour
                for pixel in range(5, self.number_of_neopixels):
                    cp.pixels[pixel] = self.colour_black

            cp.pixels.show()

    def control_feedback_y(self, acceleration_y):
        if acceleration_y <= 9.81 and acceleration_y >= -9.81 :
            converted_y_val = acceleration_y /(9.8/127)


            colour = [0, 0, converted_y_val]
            cp.pixels.fill(colour)
            cp.pixels.show()
        else:
            return None

    def control_feedback_x(self, acceleration_x):
        if acceleration_x > 2:
            if acceleration_x <= 9.81 and acceleration_x >= -9.81 :
                converted_x_val = ((acceleration_x -2) * 177 / 7.81) +177

                #print(converted_x_val)
                #print(acceleration_x)

                colour = [0, 0, converted_x_val]
                print(colour)
                cp.pixels.fill(colour)
        else:

            cp.pixels.fill(self.colour_black)
        cp.pixels.show()


    def control_feedback(self, acceleration_x, colour):
        if acceleration_x <= 9.81 and acceleration_x >= -9.81 :
            cp.pixels.fill(self.colour_black)
            if acceleration_x > 2:


                converted_x_val = (acceleration_x - 2) * 5 / 7.81

                converted_x_val = round(converted_x_val)

                new_list = []
                #init list
                i = 4

                while i >= converted_x_val:
                    #create a reversed list
                    new_list.append(i)
                    i -= 1

                converted_x_val = (acceleration_x -2)* 127 / 7.81 +127

                print(converted_x_val)
                #print(acceleration_x)

                colour = [0, converted_x_val, 255]
                #print(colour)

                for i in new_list:

                    cp.pixels[i] = colour


            elif acceleration_x < -2:


                converted_x_val_left = ((((acceleration_x * -1) -2) * 5) /7.81 ) + 4

                converted_x_val_left = round(converted_x_val_left)

                new_list = []
                acceleration_x_polarised = acceleration_x * -1
                converted_x_val2 = ((acceleration_x_polarised -2)* 127 / 7.81) + 126
                #here I added 126 to the converted value to make sure the colour values go from 126 to 255

                print(converted_x_val2)
                #print(acceleration_x)

                colour = [0, converted_x_val2, 255]
                for i in range(5, converted_x_val_left + 1):
                    new_list.append(i)

                for i in new_list:

                    cp.pixels[i] = colour

            else:

                   cp.pixels.fill(self.colour_black)
            cp.pixels.show()
