#Import pygame
import pygame
#Initilaize pygame
pygame.init() 
#Create the screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Breakout Game")
#Create paddle
paddle=pygame.Rect(300,500,60,10)
#Create ball
ball=pygame.Rect(200,250,10,10)
#Create ballx
ballx=-1
#Create bally
bally=-1
#Create paddlex
paddlex=2
#Create "carryOn"
carryOn = True
#Begin while loop
while carryOn:
  #Use for loop to check for each event
    for event in pygame.event.get(): # User did something
            #Check is quit is pressed
            if event.type == pygame.QUIT: # If user clicked close
                  #Change carryOn to False
                  carryOn = False # Flag that we are done so we exit this loop 
    #Fill screen
    screen.fill((36,90,190))
      
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=paddlex
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=paddlex
           
    pygame.draw.rect(screen,(0,176,240),paddle)
    ball.x=ball.x+ballx
    ball.y=ball.y+bally
    if ball.x>=590:
        ballx=-ballx
    if ball.x<=10:
        ballx=-ballx
    if ball.y>=590:
        bally=-bally
    if ball.y<=10:
        bally=-bally
    if paddle.collidepoint(ball.x,ball.y):
        bally=-bally
   
    pygame.draw.rect(screen,(255,255,255) ,ball)
    
    for i in range(7):
        brick=pygame.Rect(10 + i* 100,60,80,30)
        pygame.draw.rect(screen,(255,0,0),brick)
    #Create orange brick here
    
    pygame.time.wait(10)
    pygame.display.flip()
pygame.quit()
    
