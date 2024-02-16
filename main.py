# Importing the library
import pygame
pygame.init()

fps = 1
clock = pygame.time.Clock()
sc = 720
screenDimension = (sc,sc*3/4)
boardDimension = int(screenDimension[1]*0.8)
squareSize = boardDimension//8
xOffset=(screenDimension[0]-boardDimension)//2
yOffset=(screenDimension[1]-boardDimension)//2
screen = pygame.display.set_mode((screenDimension[0],screenDimension[1]))
whiteCheck = (227,193,111)
blackCheck = (184,139,74)
borderColor = (21,21,21)
black = (21,21,21)
white = (222,217,182)
screen.fill(blackCheck)
for y in range(0,boardDimension,squareSize):
    if y%(squareSize*2)==0: s = squareSize 
    else: s = 0
    for x in range(s,boardDimension,squareSize*2):
        pygame.draw.rect(screen, whiteCheck, pygame.Rect(x+xOffset, y+yOffset, squareSize, squareSize))
pygame.draw.rect(screen, borderColor, pygame.Rect(xOffset-1, yOffset-1, squareSize, squareSize))
    
pygame.display.flip()
running = True
while running:
   pygame.display.flip() 
