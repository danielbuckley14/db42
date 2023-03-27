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
      desc = "This class creates an instance of a bullet. using only private instance variables the bullet has: x coordinates %s and y coordinates %s, a radius of %s a colour of %s and a speed of %s" % (self.__bullet_x, self.__bullet_y, self.__radius, self.__bullet_color, self.__bullet_speed_y)
      
      #we get the priavte instance variable using our filename getter
      return desc
   
   def draw_Bullet(self, display):
      #print(self.__bullet_coordinates)
      pygame.draw.circle(display, self.__bullet_color, self.__bullet_coordinates, self.__radius)

  
   def move(self, pos: list):
      '''
      dir parameter not included as bullet will only be travelling vertically
      
      '''
      if self.__triggered == True:
         # if the trigger is set to true, we move bullet verticallys
         self.__bullet_y -= self.__bullet_speed_y
         self.__bullet_coordinates = [self.__bullet_x, self.__bullet_y]
         #we update coorrds
      
      else:
         #if riggers not set we move bullet relative to paddle
         self.__bullet_x = pos[0]
         self.__bullet_y = pos[1]
         
         self.__bullet_coordinates = [self.__bullet_x, self.__bullet_y]
         

   def set_trigger(self, triggered: bool):
      '''
      
      this method sets the trigger to true if the a boolean is passed in 
      '''
      if triggered:
         self.__triggered = True
         #we set instance var to true
      

   def wall_collision(self):
      '''
      if we collide with back wall we rest
      '''
      if self.__bullet_y <= self.__radius:
         #if bullet hits back wall we set trigger to false which causes bullet to move rel to paddle
         self.__triggered = False
   #we create getters and setters to access variables outside class


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
   
   def Get_Speed_x(self):
      return self.__bullet_speed_y


   def Get_Speed_y(self):
      return self.__bullet_speed_y


   def Get_coordinates(self):
      return self.__bullet_coordinates
   
   def Set_coordinates(self, coords):
      self.__bullet_coordinates = coords