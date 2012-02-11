#!/usr/bin/env python -tt

#check this change



import sys
import pygame
from pygame.locals import *   #consider explicit import

#continuously add vars until development is done :)
#from vogelConfigurations import ( FULLSCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, TOP_MARGIN, 
#                                  BOTTOM_MARGIN, CENTER_MARGIN, LEFT_MARGIN, RIGHT_MARGIN, 
#                                  BLOCK_SIZE, FORCE_BLOCK_SIZE_STATIC, WEALTH_OF_COLORS, 
#                                  FORCE_NO_CLUSTER, FORCE_EQUIDISTANT, FORCE_BILATERALLY_EQUAL,
#                                  STIMULUS_FLASH_TIME, WAIT1, WAIT2, WAIT3, BLACK, WHITE, RED, 
#                                  GREEN, BLUE, YELLOW, GREY, AQUA, SNOW, SNOW2, 
#                                  FRAMES_PER_SECOND, WINDOW_CAPTION, BACKGROUND, CROSS_COLOR, 
#                                  CROSS_WIDTH, LINE_WIDTH )   ####
from vogelConfigurations import *



def main():
    def draw_cross():
        pygame.draw.line( screen, CROSS_COLOR, (
                                    CENTRE_COORDINATE_X,CENTRE_COORDINATE_Y-CROSS_WIDTH*WINDOW_WIDTH), 
                                    (CENTRE_COORDINATE_X,CENTRE_COORDINATE_Y+CROSS_WIDTH*WINDOW_WIDTH), 
                                    LINE_WIDTH )
        pygame.draw.line( screen, CROSS_COLOR, (
                                CENTRE_COORDINATE_X-CROSS_WIDTH*WINDOW_WIDTH,CENTRE_COORDINATE_Y), 
                                   (CENTRE_COORDINATE_X--CROSS_WIDTH*WINDOW_WIDTH,CENTRE_COORDINATE_Y), 
                                   LINE_WIDTH )

    def draw_arrow( direction ):
        if direction == "left":
            pygame.draw.polygon( screen, CROSS_COLOR, 
                             [ ( CENTRE_COORDINATE_X - ARROW_X_OFFSET,
                                        CENTRE_COORDINATE_Y-ARROW_Y_OFFSET),
                             ( CENTRE_COORDINATE_X - ARROW_X_OFFSET + ARROW_X_SPAN,
                                        CENTRE_COORDINATE_Y - ARROW_Y_OFFSET + ARROW_Y_SPAN),
                            (CENTRE_COORDINATE_X - ARROW_X_OFFSET + ARROW_X_SPAN,
                                        CENTRE_COORDINATE_Y - ARROW_Y_OFFSET - ARROW_Y_SPAN)], 0 )  
            pygame.draw.line( screen, CROSS_COLOR, 
                                         (CENTRE_COORDINATE_X-ARROW_X_OFFSET, 
                                                           CENTRE_COORDINATE_Y-ARROW_Y_OFFSET),
                                         (CENTRE_COORDINATE_X+ARROW_X_OFFSET, 
                                                           CENTRE_COORDINATE_Y-ARROW_Y_OFFSET), 1 )
        if direction == "right":
            pygame.draw.polygon( screen, CROSS_COLOR, 
                             [ ( CENTRE_COORDINATE_X + ARROW_X_OFFSET,
                                        CENTRE_COORDINATE_Y-ARROW_Y_OFFSET),
                             ( CENTRE_COORDINATE_X + ARROW_X_OFFSET - ARROW_X_SPAN,
                                        CENTRE_COORDINATE_Y - ARROW_Y_OFFSET + ARROW_Y_SPAN),
                            (CENTRE_COORDINATE_X + ARROW_X_OFFSET - ARROW_X_SPAN,
                                        CENTRE_COORDINATE_Y - ARROW_Y_OFFSET - ARROW_Y_SPAN)], 0 )  
            pygame.draw.line( screen, CROSS_COLOR, 
                                         (CENTRE_COORDINATE_X-ARROW_X_OFFSET, 
                                                           CENTRE_COORDINATE_Y-ARROW_Y_OFFSET),
                                         (CENTRE_COORDINATE_X+ARROW_X_OFFSET, 
                                                           CENTRE_COORDINATE_Y-ARROW_Y_OFFSET), 1 )
    
    def draw_blocks():
        pass



    pygame.init()
    
    if FULLSCREEN:
        possible_sizes = pygame.display.list_modes( 0, pygame.FULLSCREEN )
        WINDOW_WIDTH = possible_sizes[0][0]
        WINDOW_HEIGHT = possible_sizes[0][1]
        screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN )
    else:
        screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
    
    
    CENTRE_COORDINATE_X = WINDOW_WIDTH / 2
    CENTRE_COORDINATE_Y = WINDOW_HEIGHT / 2 
        
    pygame.display.set_caption( WINDOW_CAPTION )
    clock = pygame.time.Clock()
    screen.fill( BACKGROUND )
    
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit( 0 )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
        
        
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        draw_cross()
        draw_arrow( "right" )
        draw_arrow( "left" )
        draw_blocks()
    
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
         
        
        
        clock.tick( FRAMES_PER_SECOND )
        pygame.display.flip()
    
    
    pygame.quit()


if __name__ == "__main__":
    main()


