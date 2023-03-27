import pygame

class Paddle:
    def __init__(self, px, py, paddle_WIDTH, paddle_HEIGHT, paddle_color, paddle_speed):
        
        #we create a private instance variable
        print("instance of FileReader class created!")
        self.__paddle_color = paddle_color
        self.__paddle_HEIGHT = paddle_HEIGHT
        self.__paddle_WIDTH = paddle_WIDTH
        self.__paddle_x = px
        self.__paddle_y = py
        self.__paddle_speed = paddle_speed
        self.__paddle_coordinates = [self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT]
        #all instance variables were made private to ensure that that variables were not accidentally overwritten or changed 
        #if we were to instantiate more paddles for multiplayer games for example we might not want variable to be shared across all instances of the class
        #it may be useful for example that the paddles would be of different colors
        
    def __str__(self):
        
        #here we describe the instance of the class
        desc = "This class creates an instance of a paddle. using only private instance variables the paddle has: x coordinates %s and y coordinates %s, a width of %s a height of %s and a speed of %s" % (self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT, self.__paddle_speed)

        #we get the priavte instance variable using our filename getter
        return desc
    #we define getters and setters for each of our instance variables to access them outside the class
 

    def draw_paddle(self, display):
        
        pygame.draw.rect(display, self.__paddle_color, pygame.Rect(self.__paddle_coordinates),  2, 2, 2, 2)
    #we draw the paddle by passing in display color and position params into draw function
    def move_left(self, left_trigger):

        '''
        This function moves the paddle left if its inside the the screen borders
        assums we do not to pass in display width as its not need when dealing with the left side of screen
        '''
        #we didnt pass in anything in for display size as the left border of the screen always has an x coordinate of zero
        what_key = pygame.key.get_pressed()
            #this returns a list of the state of all keys we then check if the key pressed matches the left arrow
        if what_key[left_trigger]:
            #if left trigger is the left key it will match with the corresponding leftKey in the list of keys
            if self.__paddle_x > 0:
                #if the x coord is inside the left edge of the screen we can move further left
                self.__paddle_x -= self.__paddle_speed
                #we decrement the x coord
                self.__paddle_coordinates = [self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT]
                #we update the coords
        self.__paddle_coordinates = [self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT]
        
       
        
    def move_right(self, right_trigger, display_width):
        '''
        this method moves the paddle right
        '''
        what_key = pygame.key.get_pressed()
        #we store the key pressed into what_key
        if what_key[right_trigger]:
            #this returns a list of the state of all keys we then check if the key pressed matches the right arrow

            if self.__paddle_x < display_width - self.__paddle_WIDTH:
                #we check if the right side of the paddle is inside the bounds of the screen by subtracting the width
                self.__paddle_x += self.__paddle_speed
                #if its inside the screen width we can move further right
                self.__paddle_coordinates = [self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT]
                #we update coords
            
        self.__paddle_coordinates = [self.__paddle_x, self.__paddle_y, self.__paddle_WIDTH, self.__paddle_HEIGHT]

        
    # we create getters and setters to change private instance variables outside of class
    def Get_x_coord(self):
        return self.__paddle_x
    
    
    def Set_x_coord(self, x):
        self.__paddle_x = x
    
    def Set_y_coord(self, y):
        self.__paddle_y = y 

    def Get_y_coord(self):
        return self.__paddle_y
    
    def Get_Paddle_Width(self):
        return self.__paddle_WIDTH
    
    def Set_Paddle_Width(self, width):
        self.__paddle_WIDTH = width

    def Get_Paddle_Height(self):
        return self.__paddle_HEIGHT
    
    def Set_Paddle_Height(self, height):
        self.__paddle_HEIGHT = height


    def get_color(self):
        #we get the colour
        return self.__paddle_color
    
    def set_color(self, color):
        #we get the colour
        self.__paddle_color = color

   
    
   