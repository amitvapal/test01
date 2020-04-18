'''
Student Name: 
Game title:
Period:
Features of Game: 
'''

import pygame, sys, random                                    #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=600                                                  #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Line Art")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

def randomColor():
    
    r= random.randint(0,250)
    g= random.randint(0,250)
    b= random.randint(0,250)
    return (r,g,b)

def drawLines(xa, ya, color, numS):
    xgap = int(w/numS)
    ygap = int(h/numS)
    # check to see if we neeed to move left or right
    if xa == [w,0]:
        xgap *= -1
    elif ya == [w,h]:
        ygap *= -1
    
        
    for i in range (numS):
        xa[0] += xgap
        ya[1] += ygap
        pygame.draw.line(surface, color, xa, ya,1)
        



# -------- Main Program Loop -----------
def main():
    
    userInput = int(input("Please enter a number of lines: "))
    
    #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    color = randomColor()
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(WHITE)                             #set background color
        
        #drawing code goes here
        
        drawLines([0,h], [0,0], color, userInput)
        drawLines([0,h], [w,h], color, userInput)
        drawLines([w,0], [0,0], color, userInput)
        drawLines([0,0], [w,0], color, userInput)
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program


hello amitva