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
BLACKTOKENIMG     = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
BOARDIMG          = pygame.image.load('4row_board.png')
BOARDIMG          = pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))
HUMANWINNERIMG    = pygame.image.load('4row_humanwinner.png')
COMPUTERWINNERIMG = pygame.image.load('4row_computerwinner.png')
TIEWINNERIMG      = pygame.image.load('4row_tie.png')

WINNERRECT        = HUMANWINNERIMG.get_rect()
WINNERRECT.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
ARROWING          = pygame.image.load('4row_arrow.png')
ARROWRECT         = ARROWIMG.get_rect()
ARROWRECT.left    = REDPILERECT.right + 10
ARROWRECT.centery = REDPILERECT.centery


def drawBoard(board, extraToken=None):
	DISPLAY.fill(BGCOLOR)
	spaceRect = pygame.Rect(0, 0, SPACESIZE, SPACESIZE)
	for x in range(BOARDWIDTH):
