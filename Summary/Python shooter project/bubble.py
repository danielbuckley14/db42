import pygame
import random
class Bubble:
   def __init__(self, x, y, radius, bubble_color, bubble_speed_x, bubble_speed_y):
      
   #we create a private instance variable
      '''
      Again we use all private instance variable so as not to accidentally overwrite variables
      it also promotes reuse and allows us the ability to create multiple bubbles to shoot at
      '''
      print("instance of FileReader class created!")
     
      self.__bubble_color = bubble_color
      self.__radius = radius
      self.__bubble_x = x
      self.__bubble_y = y
      self.__bubble_coordinates = [self.__bubble_x, self.__bubble_y]
      self.__bubble_speed_x = bubble_speed_x
      self.__bubble_speed_y = bubble_speed_y
      
   def __str__(self):
      
      #here we describe the instance of the class
      desc = "This class creates an instance of a bubble. Using only private instance variables the bubble has: x coordinates %s and y coordinates %s, a radius of %s, a colour of %s, vertical speed of %s and a horizontal speed of %s. The paddle is given the rgb colour of %s \n" % (self.__bubble_x, self.__bubble_y, self.__radius, self.__bubble_color, self.__bubble_speed_y, self.__bubble_speed_x, self.__bubble_color)      #we get the priavte instance variable using our filename getter
      return desc
   
   #we draw the bubble 
   def draw_Bubble(self, display):
      #we draw the bubble to the display
      # #we need to remember that when we update position of the bullet we need to update the coordinates variable
      pygame.draw.circle(display, self.__bubble_color, self.__bubble_coordinates, self.__radius)

      
   def move(self, horizontal_bound, vertical_bound):
      '''
      this method moves the bubble diagonally down the screen and features a bouncing effect 
      when bubble hits the wall
      '''
      intilising_counter = 0
      #we initialise counter so as this if statement will only be needed once
      if self.__bubble_y <= (self.__radius ) and intilising_counter == 0:
         #if the bubble is at the top of the screen we randomly relocate it on the x axis
         random_x_val = self.relocate(horizontal_bound, vertical_bound)
         #we set it to position within the bounds of the width of the screem
         self.__bubble_x = random_x_val
         #we set the x coordinate to the random position
         intilising_counter +=1
         #we inc counter to prevent if statement from running again 
     
      if self.__bubble_x >= horizontal_bound - self.__radius:
         #if the bubble hits the right has side of the screen we polarise its speed to send it in the opposite direction
         self.__bubble_speed_x = self.__bubble_speed_x * -1
         
      if self.__bubble_x - self.__radius <= 0: 
         # if the left side of the bubble hits the left side 
         #we polarise the speed of the bubble to send it in the opposite direction
         self.__bubble_speed_x = self.__bubble_speed_x * -1
      
      if self.__bubble_y >= vertical_bound - self.__radius:
         
         #if the bubble hits the line we rolocate it
         #we again use our random placement
         
         #we set the speed to be set between -4 and 4 so it goes both ways
         random_x_val = self.relocate(horizontal_bound, vertical_bound)
         #we call the relocate method to generate a random x value
         self.__bubble_x = random_x_val
         #we set the random starting point
         self.__bubble_y = self.__radius
         #we offset from the top of screen 
         random_direction = random.choice([-self.__bubble_speed_x, self.__bubble_speed_x])
         

         self.__bubble_speed_x = random_direction
         #we assign the random speed

      self.__bubble_y += self.__bubble_speed_y 
      #we incremenet the position of the bubble
      self.__bubble_x -= self.__bubble_speed_x 
      self.__bubble_coordinates = [self.__bubble_x, self.__bubble_y]
     
   #we create getters and setters to access variables outside the class

   def relocate(self, horizontal_bound, vertical_bound):
      #this method generates a random x coordinate between either side of the screen
      random_x_coord = random.uniform(0 + self.__radius, horizontal_bound - (self.__radius * 2))
      return random_x_coord

   def change_size(self, lower_limit, upper_limit):
      #this method reduces the size of the circle using the decrementer
      decrementer = 5
      if self.__radius >= lower_limit + decrementer and self.__radius <= upper_limit: 
         #if the radius is greater than the lower limit and less than the upper limit we decrement
         self.__radius -= decrementer
         
   '''
   Here I set up getters and setters to access class attributes outside the class
   This supports encapsulation whereby attributes can only be modified outside the class using getters and setters
   This prevents unintentional changes to variables by other objects
   
   '''
   def Get_x_coord(self):
      return self.__bubble_x
   
   def Get_y_coord(self):
      return self.__bubble_y
   
   def Set_x_coord(self, x):
      self.__bubble_x = x
   
   def Set_y_coord(self, y):
      self.__bubble_y = y 
   
   def Set_Bubble_Radius(self, radius):
      self.__radius = radius

   def Get_Bubble_Radius(self):
      return self.__radius 

   def Get_Speed_x(self):
      return self.__bubble_speed_y
   
   def Set_Speed_x(self, speed):
      
      self.__bubble_speed_x = speed

   def Get_Speed_y(self):
      return self.__bubble_speed_y

   def Set_Speed_y(self, speed):
      self.__bubble_speed_x = speed

  
   