# Importing the library
import pygame
import json
pygame.init()

fps = 1
clock = pygame.time.Clock()
sc = 640 #Screen size
screenDimension = (sc,int(sc*3/4))
screen = pygame.display.set_mode((screenDimension[0],screenDimension[1]))

boardDimension = int(screenDimension[1]*0.8)
squareSize = boardDimension//8
xOffset=(screenDimension[0]-boardDimension)//2
yOffset=(screenDimension[1]-boardDimension)//2

# board color pallete and design
with open('path_to_file/person.json') as f:
    colorPalletes = json.load(f)
print(colorPalletes)
default_bg = pygame.image.load("assets/background/bg.jpg")
#color pallete
borderWidth = 4
whiteCheck = (227,193,111)
blackCheck = (184,139,74)
black = (21,21,21)
white = (222,217,182)
def drawBoard(whiteSqColor=(96,104,108), blackSqColor=(44,47,49), Background=pygame.image.load("assets/background/bg.jpg"), borderSqColor=(21,21,21)):
    screen.blit(Background, (0, 0))
    for y in range(0,boardDimension,squareSize):
        for x in range(0,boardDimension,squareSize):
            if ((y+x-2)//squareSize)%2==0:
                pygame.draw.rect(screen, whiteSqColor, pygame.Rect(x+xOffset, y+yOffset, squareSize, squareSize))
            else:
                pygame.draw.rect(screen, blackSqColor, pygame.Rect(x+xOffset, y+yOffset, squareSize, squareSize))
    pygame.draw.rect(screen, borderSqColor, pygame.Rect(xOffset-1, yOffset-1, boardDimension+2, boardDimension+2), 1) 
drawBoard() 
# drawBoard(whiteCheck,blackCheck)
pygame.display.flip()
running = True
while running:
   pygame.display.flip() 
