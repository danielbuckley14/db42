import math
import pygame
#we import pygame
from paddle import Paddle
#from the paddle file we import the Paddle class
from bullet import Bullet
#from the bullet file we import the Bullet class
from bubble import Bubble
#from the bubble file we import the Bubble class
import random
pygame.init()

'''
in this main file we import three class
we instantiate these classes as objects 
these objects will eventually be able to interact with interact with one another to create the final game

'''
#we intilise the pygame modules
#always assign to variables
DISPLAY_WIDTH = 500
#we set the screen width
DISPLAY_HEIGHT = 500
#we set the screen height
WHITE = [255, 255, 255]
#we creste the colour for the background of the diplay
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
#we store diplay width and height into a list
display = pygame.display.set_mode(DISPLAY_SIZE)
#we pass display size into a function that creates the ui

#setting up the paddle

paddle_color = [0, 0, 0]
#we set the paddle colour 
paddle_HEIGHT = 10
#we create a paddle height and width
paddle_WIDTH = 200
paddle_x = DISPLAY_WIDTH// 2 - (paddle_WIDTH//2)

#using half the display width and by subtracting paddle
#  width we position the paddle in the middle of screen
paddle_y = DISPLAY_HEIGHT - paddle_HEIGHT
#in order to position the paddle at the bottom of the screen 
# we subtract the paddle height from the display height as both the 
# display and paddle are drawn from top left corner
paddle_speed = 5
#we set the paddle speed which is the apparent speed that the paddle will move
paddle_1 = Paddle(paddle_x, paddle_y, paddle_WIDTH, paddle_HEIGHT, paddle_color, paddle_speed)
#we create an instance of the Paddle class by passing in the previously initialised vars
#I have stored created variable for each passed in parameter as its for more readable when making changes

#setting up bullet
#this can be commented out
bullet_color = [0, 200, 200]
#bullet will be black 
bullet_radius = 40
#we set bullet radius
bullet_x = paddle_1.Get_x_coord() + (paddle_1.Get_Paddle_Width() // 2)# 600 // 2 = 300
#we set the bullet x coordinate to be relative to the paddle class as they will always appear relative to one another
#we use the paddle x coordinate and add half of the paddle
#the bullet is drawn from the center so no need to worry about offsetting
bullet_y = paddle_1.Get_y_coord() - bullet_radius 
#we try and position the bullet atop the paddle by subtracting the bullet radius from the 
# coordinates for the top of the paddle 


bullet_speed_y = 10 
#this is the speed that the bullet will move when triggered
#no xspeeded needed as bullet will move relative to the coordinates of the paddle

bullet_1 = Bullet(bullet_x, bullet_y, bullet_radius, bullet_color, bullet_speed_y)
#we create an instance of the Bullet class and pass in our vars 

#setting up the bubble
bubble_color = [252, 231, 3]
# the bubble will be black
bubble_radius = 40
#set radius
bubble_x = DISPLAY_WIDTH
#we center the bubble in the middle of the screen
bubble_y = 0 + (bubble_radius)
#we position it at top of screen remembering that circles are drawn from origon
bubble_speed_x = 4
#the bullet will be moving diagonally so it needs  both a lateral and vertical speed
# in order to show that the bubble can bounce of the walls we make it move faster horizontally
bubble_speed_y = 2
bubble_1 = Bubble(bubble_x, bubble_y, bubble_radius, bubble_color, bubble_speed_x, bubble_speed_y)
#we create an instance of the bubble class
clock = pygame.time.Clock()
# use the time function to initialise our clock in order to set refresh rate later
#we set the vertical bound which will remain contstant throughout application
#the line is drawn outise of a class
vertical_bound = round(DISPLAY_HEIGHT/ 2)

# setup of booleans

run_game = True
#we initialise run game and set to true until user closes ui
count = 0
#we intialise count, which prevents bullet from showing until after it is shot for the first time


def collision_check(object1, object2, height):
    '''
    This function checks if two objects have collided I pass in the two objects as arguments
    This supports reuse as we could potentially pass in different instances of bullet and bubble objects
    If a consistent naming convention was used across objects we could check collisions for any displayed circles
    
    '''
    distance_paddle_bullet = math.sqrt(((object1.Get_x_coord() - object2.Get_x_coord())**2) + ((object1.Get_y_coord() - object2.Get_y_coord())**2))
    #we use the euclidian distance formula which we learned in coordinate geometry to find the straight line dist between two points
    if distance_paddle_bullet <= (object1.Get_Bubble_Radius() + object2.Get_Bullet_Radius()):
        #if the distance is less than the sum of the radii objects are colliding
        random_x_val = object1.relocate(DISPLAY_WIDTH, height)
        #we call the relocate function to generate a random x vall
        object1.Set_x_coord(random_x_val) 
        #we set the random starting point
        random_direction = random.choice([-object1.Get_Speed_x(), object1.Get_Speed_x()])
        #we generate a random speed
        object1.Set_y_coord(object1.Get_Bubble_Radius()) 
        #we offset from the top of screen 
        object1.Set_Speed_x(random_direction) 
        #we set the speed of the bullet to -speed or + speed to give it a random direction
        object2.set_trigger(False)
        #to return the 
        object1.change_size(30, bubble_radius)
        object2.change_speed(2, bullet_1.Get_Speed_y())
        
        
#print(paddle_1.__str__())
#print(bullet_1.__str__())
#print(bubble_1.__str__())
#my string representations
while run_game:
    
    display.fill(WHITE)
    #we set the background colour using our white variable
    paddle_1.draw_paddle(display)
    #we call our draw method to by passing and pass in our display variable
    bubble_1.draw_Bubble(display)
    #we call our draw method to by passing and pass in our display variable
    collision_check(bubble_1, bullet_1, vertical_bound)
    

    pygame.draw.line(display, (0,0,255), (0, vertical_bound), (DISPLAY_WIDTH, vertical_bound))
    #we draw the line 
    #vertival bound we later be used to check if the bubble has hit the line
    for event in pygame.event.get():
        #this for loop checks for events
        #while the game is running this listens for events 
        if event.type == pygame.QUIT:
            #if the user quits we set run game to false and end the game
            run_game = False
        if event.type == pygame.KEYDOWN:
            #if a key is pressed we..
            if event.key == pygame.K_SPACE:
                #check if it was the space bar
                bullet_1.set_trigger(True)
                #we set the trigger to true
                count += 1
                #we increment count so that bullet will be displayed
    
    bubble_1.move(DISPLAY_WIDTH, vertical_bound)

    #we tell bubble to move and pass in our bounds 
    paddle_1.move_left(pygame.K_LEFT)
    #we pass the left key into the move method
    #these methods are contantly running in order to detect when a key is pressed
    paddle_1.move_right(pygame.K_RIGHT, DISPLAY_WIDTH)
    #we pass the right key into the move method
    

    if count >= 1:
        #if the user has pressed the space bar the count is not == to 1
        bullet_1.draw_Bullet(display)
        
        #we draw the bullet   
        bullet_1.move([paddle_1.Get_x_coord() + (paddle_1.Get_Paddle_Width()//2), paddle_1.Get_y_coord() - bullet_1.Get_Bullet_Radius() ])
        #we call the move method and if the trigger = true we shoot bullet if not we move bullet  
        #according relative to coordinates of paddle
        bullet_1.wall_collision()
        #if the bullet collides with the back wall we set trigger == to false and reset bullet
    else:
        
        bullet_1.Set_coordinates( [paddle_1.Get_x_coord() + (paddle_1.Get_Paddle_Width()//2), paddle_1.Get_y_coord() - bullet_1.Get_Bullet_Radius()])
        #this updates the coordinates of the bullet when the paddle is moved before the bullet is first triggered
    
    pygame.display.update()
    #we refresh the frame 
    clock.tick(60)
    #we set our refresh rate
pygame.quit()
#if we exit the above while loop we close the pygame library and end the program
quit()