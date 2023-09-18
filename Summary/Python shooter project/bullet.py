import pygame

class Bullet:
   def __init__(self, x, y, radius, bullet_color, bullet_speed_y):
      
      #we create a private instance variable
      print("instance of FileReader class created!")
      self.__bullet_color = bullet_color
      self.__radius = radius
      self.__bullet_x = x
      self.__bullet_y = y
      self.__bullet_coordinates = [self.__bullet_x, self.__bullet_y]
      self.__bullet_speed_y = bullet_speed_y
      self.__triggered = False
   def __str__(self):
        
      #here we describe the instance of the class
      desc = "This class creates an instance of a bullet. Using only private instance variables the bullet has: x coordinates %s and y coordinates %s, a radius of %s, a rgb colour of %s and a speed of %s \n" % (self.__bullet_x, self.__bullet_y, self.__radius, self.__bullet_color, self.__bullet_speed_y)
      return desc
   
   def draw_Bullet(self, display):
      #this method draws the bullet to the display 
      #we need to remember that when we update position of the bullet we need to update the coordinates variable
      pygame.draw.circle(display, self.__bullet_color, self.Get_coordinates(), self.__radius)

  
   def move(self, pos: list):
      '''
      inputs pos here we pass in the position the bullet should move to when not triggered
      This method updates the coordinates of the bullet
      dir parameter not included as bullet will only be travelling vertically
      
      '''
      
      if self.__triggered == True:
         #when the space bar is pressed self.__triggered is set to true 
         #this if statement will then run
         if self.__bullet_y >= pos[1]:
            #this line ensure the position of the bullet is updated before it is fired
            #i update on the condition that the bullet y position is less than or equal to the top of the paddle
            #this ensures the user cannot change the position of the bullet after it has been triggered
            self.__bullet_x = pos[0]
            #we update the x position of the bullet
         # if the trigger is set to true, we move bullet vertically
         self.__bullet_y -= self.__bullet_speed_y
         
         
         self.__bullet_coordinates = [self.__bullet_x, self.__bullet_y]
         #we update coorrds
      
      else:
         #if riggers not set we move bullet relative to paddle
         self.__bullet_x = pos[0]
         self.__bullet_y = pos[1]
         #we assign the passed in values to the x and y coords
         self.__bullet_coordinates = [self.__bullet_x, self.__bullet_y]
      
      

   def set_trigger(self, triggered: bool):
      '''
      input: boolean which sets checks if boolean is true 
      sets triggered to true if boolean arg is true
      '''
      if triggered:
         self.__triggered = True
         #we set instance var to true
      else:
         self.__triggered = False
      

   def wall_collision(self):
      '''
      if we collide with back wall we rest
      '''
      if self.__bullet_y <= self.__radius:
         #if bullet hits back wall we set trigger to false which causes bullet to move rel to paddle
         self.__triggered = False
      #we create getters and setters to access variables outside class


   def change_speed(self, lower_limit, upper_limit):
      decrementer = 2
      #we hardcode the decrementer value
      if self.__bullet_speed_y - decrementer >= lower_limit and self.__bullet_speed_y <= upper_limit:  
         #if the speed is greater than the lower limit and less than the upper limit we decrement the speed
         self.__bullet_speed_y -= decrementer
     
   '''
   Here I set up getters and setters to access class attributes outside the class
   This supports encapsulation whereby attributes can only be modified outside the class using getters and setters
   This prevents unintentional changes to variables by other objects
   
   '''
   def Get_x_coord(self):
      return self.__bullet_x
   
   def Get_y_coord(self):
      return self.__bullet_y
   
   def Set_x_coord(self, x):
      self.__bullet_x = x
   
   def Set_y_coord(self, y):
      self.__bullet_y = y 
   
   def Set_Bullet_Radius(self, radius):
      self.__radius = radius

   def Get_Bullet_Radius(self):
      return self.__radius
   
  


   def Get_Speed_y(self):
      return self.__bullet_speed_y


   def Get_coordinates(self):
      return self.__bullet_coordinates
   
   def Set_coordinates(self, coords):
      self.__bullet_coordinates = coords