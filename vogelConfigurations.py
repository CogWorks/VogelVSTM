#!/usr/bin/python


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (148, 0, 211)
GREY = (128, 128, 128)
AQUA = (0, 255, 255)
SNOW1 = (238, 233, 233)
SNOW2 = (205, 201, 201)

FULLSCREEN = True 
WINDOW_HEIGHT = 500   # overridden by fullscreen bool
WINDOW_WIDTH = 700   # overridden by fullscreen bool

TOP_MARGIN = 10
BOTTOM_MARGIN = 10
CENTRE_MARGIN = 30   #away from fixation cross
LEFT_MARGIN = 10
RIGHT_MARGIN = 10

BLOCK_SIZE = .05   # ratio of block width to screen width
NUMBER_OF_BLOCKS = 3
FORCE_BLOCK_SIZE_STATIC = False   
WEALTH_OF_COLORS = 5   # max different colors
FORCE_NO_CLUSTER = False  
FORCE_EQUIDISTANT = False 
FORCE_BILATERALLY_EQUAL = False 


WAIT1 = 1000   # between "ready?" and cross drawn
WAIT2 = 1000   #between cross drawn and arrow drawn
ARROW_FLASH_TIME = 200
WAIT3 = 300   #between arrow drawn and stimulus flash
STIMULUS_FLASH_TIME1 = 100
WAIT4 = 900   # between first flash and second flash
STIMULUS_FLASH_TIME2 = 2000
WAIT5 = 500   # between second flash and "same or different?"
#WAIT6 = 1000   #between "same or different?" answer and ....#####


FRAMES_PER_SECOND = 2000
WINDOW_CAPTION = "Vogel Task"
BACKGROUND = SNOW1

CROSS_WIDTH = .008   # ratio of fixation cross width and screen width
LINE_WIDTH = 2
CROSS_COLOR = BLACK

ARROW_X_OFFSET = 40
ARROW_X_SPAN = 15
ARROW_Y_OFFSET = 70
ARROW_Y_SPAN = 5

CROSS_DISAPPEARS_ON_ARROW = False


"""
pygame.draw.line( screen, CROSS_COLOR, (0,0), (WINDOW_WIDTH,WINDOW_HEIGHT), 1 )
pygame.draw.line( screen, CROSS_COLOR, (WINDOW_WIDTH,0), (0,WINDOW_HEIGHT), 1 )
"""

