import random, copy, sys, pygame
from pygame.locals import *

BOARDWIDTH        =   7 # the width of board
BOARDHEIGHT       =   6 # the height of board

assert BOARDWIDTH >= 4 and BOARDHEIGHT >= 4, 'Board must be at least 4x4'

DIFFICULTY        =   2
SPACESIZE         =  50
FPS               =  30
WINDOWWIDTH       = 640
WINDOWHEIGHT      = 480

XMARGIN           = int((WINDOWWIDTH  - BOARDWIDTH  * SPACESIZE) / 2)
YMARGIN           = int((WINDOWHEIGHT - BOAEDHEIGHT * SPACESIZE) / 2)

BRIGHTBLUE        = (  0,  50, 255)
WHITE             = (255, 255, 255)

BGCOLOR           = BRIGHTBLUE
TEXTCOLOR         = WHITE

RED               = 'red'
BLACK             = 'black'
EMPTY             = 'None'
HUMAN             = 'human'
COMPUTER          = 'computer'

pygame.init()

FPSCLOCK          = pygame.time.Clock()
DISPLAYSURF       = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption(u'four in row')

REDPILERECT       = pygame.Rect(int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)

BLACKPILERECT     = pygame.Rect(WINDOWWIDTH - int(3 * SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
REDTOKENIMG       = pygame.image.load('4row_red.png')
REDTOKENIMG       = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
BLACKTOKENIMG     = pygame.image.load('4row_black.png')
REDTOKENIMG       = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
