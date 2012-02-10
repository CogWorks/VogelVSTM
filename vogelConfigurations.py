#!/usr/bin/python


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
AQUA = (0, 255, 255)
SNOW = (238, 233, 233)
SNOW2 = (205, 201, 201)

FULLSCREEN = 0   #Bool   ###DOESN'T WORK CORRECTLY YET :(
WINDOW_HEIGHT = 500   # overridden by fullscreen bool
WINDOW_WIDTH = 700   # overridden by fullscreen bool

TOP_MARGIN = 10
BOTTOM_MARGIN = 10
CENTER_MARGIN = 30   #away from fixation cross
LEFT_MARGIN = 10
RIGHT_MARGIN = 10

BLOCK_SIZE = .05   # ratio of block width to screen width
FORCE_BLOCK_SIZE_STATIC = 0    # Bool
WEALTH_OF_COLORS = 5   # max different colors
FORCE_NO_CLUSTER = 0    # Bool
FORCE_EQUIDISTANT = 0   # Bool
FORCE_BILATERALLY_EQUAL = 0   # Bool

STIMULUS_FLASH_TIME = 100
WAIT1 = 100   # between "ready?" and first flash
WAIT2 = 100   # between first flash and second flash
WAIT3 = 100   # between second flash and "same or different?"

FRAMES_PER_SECOND = 20
WINDOW_CAPTION = "Vogel Task"
BACKGROUND = SNOW2

CROSS_WIDTH = .05   # ratio of fixation cross width and screen width
LINE_WIDTH = 2
CROSS_COLOR = BLACK
