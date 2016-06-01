# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
# Import the modules needed
import pygame
import time
import socket
import sys

# Creates a datagram UDP socket 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# If an error occurs while attempting to create;
except socket.error:
    # Print an error message
    print "An error has occured: Failed to create socket"
    sys.exit()

# Set server "IP"/host 
host = 'localhost';
# Set port to use
port = 5000;

pygame.init()

# Resolution of the game
displayx=1280
displayy=720

# Define RGB values of different colors used
white = (255,255,255)
black = (0,0,0)
sky = (199,237,243)


gameDisplay = pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption('The River Crossing Game')
clock = pygame.time.Clock()

# Define file used for "dock"
dock = pygame.image.load('dock.png')
# Define file used for "dock1"
dock1 = pygame.image.load('dock1.png')
# Define file used for "river"
river = pygame.image.load('river.png')
# Define file used for "chicken"
chicken = pygame.image.load('chicken.png')
# Define file used for "farmer"
farmer = pygame.image.load('farmer.png')
# Define file used for "grain"
grain = pygame.image.load('grain.png')
# Define file used for "fox"
fox = pygame.image.load('fox.png')
# Define file used for "boat"
boat = pygame.image.load('boat.png')
# Define file used for the instructions
instructions = pygame.image.load('instructions.png')

# Define what to print if something forbidden happens
def forbidden(x):
    if x == 1:
        message("The wolf ate the chicken.. "
                "You lost the game! Try again?")
    elif x == 2:
        message("The wolf ate the chicken.. "
                "You lost the game! Try again?")
    elif x == 3:
        message("The chicken ate the grain.. "
                "You lost the game! Try again?")
 
# Define different objects on the screen,
# Which image to use and that it should have X,Y parameters
def dockImage(x,y):
    gameDisplay.blit(dock, (x,y))
    
def dockImage1(x,y):
    gameDisplay.blit(dock1, (x,y))
    
def riverImage(x,y):
    gameDisplay.blit(river, (x,y))  
    
def boatImage(x,y):
    gameDisplay.blit(boat, (x,y))
    
def chickenImage(x,y):
    gameDisplay.blit(chicken, (x,y))

def farmerImage(x,y):
    gameDisplay.blit(farmer, (x,y))

def grainImage(x,y):
    gameDisplay.blit(grain, (x,y))

def foxImage(x,y):
    gameDisplay.blit(fox, (x,y))
    
def instructs(x,y):
    gameDisplay.blit(instructions,(x,y))
    
# Define what color etc. the text should have
def textObjects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Define font, fontsize etc. for text
def message(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((displayx/2),(displayy/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    
    time.sleep(5)
    
    gameloop()

# Main
# Where objects/images should be placed
def gameloop():
    # Farmer X and Y values
    fax = 260
    fay = 580    
    faxchange = 0
    
    # Chicken X and Y values
    cx = 30
    cy = 525
    cxchange = 0
    
    # Grain X and Y values
    gx = 90
    gy = 570
    gxchange = 0
    
    # Fox X and Y values
    fox = 145 
    foy = 575
    foxchange = 0 
    
    # Boat X and Y values
    bx = 255
    by = 620
    bchange = 0
    
    victory = False
    finished = False
    
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True          
            # Define what keys are possible to use
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pass
                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_s:
                    pass
                if event.key == pygame.K_z:
                    pass                
                if event.key == pygame.K_x:
                    pass
                if event.key == pygame.K_r:
                    pass
            
            # Define what happens when the user hits different buttons                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    objct = "R"
                    try:
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        
                        if bx == 255:
                            if cx == 400:
                                cx += 565
                            elif gx == 400:
                                gx += 565
                            elif fox == 400:
                                fox += 565
                            fax += 565
                            bx += 565   
                        elif bx == 820:
                            if cx == 965:
                                cx -= 565
                            elif gx == 965:
                                gx -= 565
                            elif fox == 965:
                                fox -= 565
                            fax -= 565
                            bx -= 565
                        else:
                            pass                          
                        
                    # If an error occurs;
                    except socket.error, objct:
                        sys.exit()
                                      
                # Define what happens when the user hits "Q"
                if event.key == pygame.K_q:
                    objct = "Q"
                    try:
                        # Send the whole string
                        s.sendto(objct, (host, port))                    
                        # If gx (grain X-value) or fox (fox X-value) is NOT == 400,
                        if not gx == 400 or fox == 400:
                            # If cx (chicken X-value) is equal to 30:
                            # Add 370 to cx, 75 to cy (moves to the boat)
                            if cx == 30:
                                cx += 370 
                                cy += 75
                          
                            # If cx (chicken X-value) is equal to 1210:
                            # Subtract 245 from cx, 75 from cy (moves to the boat)
                            elif cx == 1210:
                                cx -= 245
                                cy += 75                       
                            else:
                                # Otherwise, pass
                                pass
                    # If an error occurs;
                    except socket.error, objct:
                        sys.exit()                    
                            
                if event.key == pygame.K_w:
                    objct = "W"
                    try :
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        
                        
                        if cx == 400:
                            cx -= 370 
                            cy -= 75
                        elif cx == 965:
                            cx += 245
                            cy -= 75
                        else:
                            pass                        
                    # If an error occurs; 
                    except socket.error, objct:
                        sys.exit()
                    
                if event.key == pygame.K_a:
                    objct = "A"
                    try :
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        

                        if not cx == 400 or fox == 400:
                            if gx == 90:
                                gx += 310 
                                gy += 30
                            if gx == 1170:
                                gx -= 205
                                gy += 30                        
                            else:
                                pass                        
                    # If an error occurs; 
                    except socket.error, objct: 
                        sys.exit()
                        
                if event.key == pygame.K_s:
                    objct = "S"
                    try:
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        
                        
                        if gx == 400:
                            gx -= 310 
                            gy -= 30
                        if gx == 965:
                            gx += 205
                            gy -= 30                        
                    except socket.error, objct:
                        sys.exit()

                if event.key == pygame.K_z:
                    objct = "Z"
                    try:
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        

                        if not cx == 400 or gx == 400:
                            if fox == 145:
                                fox += 255 
                                foy += 15
                            if fox == 1120:
                                fox -= 155
                                foy += 15
                    except socket.error, objct:
                        sys.exit()
                            
                if event.key == pygame.K_x:
                    objct = "X"
                    try:
                        # Send the whole string
                        s.sendto(objct, (host, port))
                        # The address
                        
                        
                        if fox == 400:
                            fox -= 255 
                            foy -= 15
                        if fox == 965:
                            fox += 155
                            foy -= 15                        
                    except socket.error, objct:
                        sys.exit()
            
            # Define what outcomes are forbidden:
            #  If bx (boat X-value) equals 820, cx (chicken X-value) equals 30, and fox (fox X-value) equals 145:
            # Display forbidden(1) message
            if bx == 820 and cx == 30 and fox == 145:
                forbidden(1)
            
            # Display forbidden(2) message    
            if bx == 255 and fox == 1120 and cx == 1210:
                    forbidden(2)            
            
            # Display forbidden(3) message        
            if bx == 255 and cx == 1210 and gx == 1170:
                        forbidden(3)
            
            # Display forbidden(3) message
            if bx == 820 and cx == 30 and gx == 90:
                forbidden(3)
            
            # If all objects are on the right bank/dock, set victory to true, player wins the game            
            if fox == 1120 and gx == 1170 and cx == 1210:
                victory = True     
    
        fax += faxchange
        cx += cxchange
        gx += gxchange
        fox += foxchange
        
        # Set background color
        gameDisplay.fill((sky))
        # Defines where different images should be placed (x, y)
        riverImage(0,650)   
        dockImage(-50,550)
        dockImage1(1080,550)
        instructs(0,0)
        farmerImage(fax,fay)
        grainImage(gx,gy)
        chickenImage(cx,cy)
        foxImage(fox,foy) 
        boatImage(bx,by)
        
        # If victory = true, display message
        if victory:
            message("You've won the game! The game will restart in 5 seconds.")
    
        pygame.display.update()
        clock.tick(60)    
        
gameloop()
pygame.quit()
quit()