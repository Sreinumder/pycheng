# Importing the library
import pygame
import json
pygame.init()

fps = 1
clock = pygame.time.Clock()
sx = 640 #Screen size
sy = int(sx*3/4)
cx = sx/2
cy = sy/2
screen = pygame.display.set_mode((sx,sy))
fontSize = 18
font = pygame.font.Font('freesansbold.ttf', fontSize) 

boardDimension = int(sy*0.8)
squareSize = boardDimension//8
xOffset=(sx-boardDimension)//2
yOffset=(sy-boardDimension)//2

# board color pallete and design
f = open('assets/palletes.json')
colorPalletes = json.load(f)
default_bg = pygame.image.load("assets/background/bg.jpg")

palleteList = list(colorPalletes.keys())

def drawBoard(whiteSqColor=(96,104,108), blackSqColor=(44,47,49), Background="bg", borderSqColor=(21,21,21)):
    Background = pygame.image.load("assets/background/"+Background+".jpg")
    screen.blit(Background, (0, 0))
    for y in range(0,boardDimension,squareSize):
        for x in range(0,boardDimension,squareSize):
            if ((y+x-2)//squareSize)%2==0:
                pygame.draw.rect(screen, whiteSqColor, pygame.Rect(x+xOffset, y+yOffset, squareSize, squareSize))
            else:
                pygame.draw.rect(screen, blackSqColor, pygame.Rect(x+xOffset, y+yOffset, squareSize, squareSize))
    pygame.draw.rect(screen, borderSqColor, pygame.Rect(xOffset-1, yOffset-1, boardDimension+2, boardDimension+2), 1) 
    pygame.display.flip()
# drawBoard(tuple(colorPalletes['cool'][0]),tuple(colorPalletes['cool'][1])) 
drawBoard(colorPalletes[palleteList[0]][0],colorPalletes[palleteList[0]][1]) 
i=0
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if i>0: i-=1
            elif event.key == pygame.K_RIGHT:
                if i<len(palleteList)-1: i+=1
            p = palleteList[i]
            print("Board pallate selection:"+p,colorPalletes[p][0],colorPalletes[p][1]) 
            drawBoard(colorPalletes[p][0],colorPalletes[p][1], p) 
            text = font.render("< "+p+" >", True, colorPalletes[p][0])
            textRect = text.get_rect()
            textRect.center = (cx, cy*1.85) 
            screen.blit(text, textRect)
            pygame.display.update()
    clock.tick(60)

running = True
while running:
   pygame.display.flip() 
