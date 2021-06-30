import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

player=pygame.Rect(0,200,20,20)
playerx=1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C5")
#Create "carryOn" variable and set to true

#Begin the while loop

  #Iterate through each event
  
    #Identify is user has quit 
    
      #change "carryOn" to False
                
  screen.fill(YELLOW)
  
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
      if player.x<=380:
        player.x=player.x+playerx
    if event.key == pygame.K_LEFT:
      if player.x>=0:
        player.x=player.x-playerx
  
  pygame.draw.rect(screen,LIGHTBLUE,player)
  pygame.display.flip()
pygame.quit()
