#Import pygame

#Initilaize pygame

#Create the screen

pygame.display.set_caption("Breakout Game")
#Create paddle

#Create ball

#Create ballx

#Create bally

#Create paddlex

#Create "carryOn"

#Begin while loop

  #Use for loop to check for each event
   
            #Check is quit is pressed
           
                  #Change carryOn to False
                 
    #Fill screen
   
      
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
    
