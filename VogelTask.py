#!/usr/bin/env python -tt

#check this change


import sys
import random
import pygame
from vogelConfigurations import *
#from vogelConfigurations import ( FULLSCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, etc.... 


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
        pygame.display.flip()

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
        pygame.display.flip()
        pygame.time.wait( ARROW_FLASH_TIME )
        clear()
        if not CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()
    
    
    #############################
    
    def draw_blocks( direction, same_or_different_flag ):
    
        real_block_size = BLOCK_SIZE * WINDOW_WIDTH
        blocksetleft1 = [ ]
        blocksetright1 = [ ]
        blocksetleft2 = [ ]
        blocksetright2 = [ ]
        
        ###################
        ### make blocks ###
        
        for position in range( NUMBER_OF_BLOCKS ):
            #blocksetleft1
            x_start = random.randrange( LEFT_MARGIN, CENTRE_COORDINATE_X - CENTRE_MARGIN - real_block_size )
            y_start = random.randrange( TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN - real_block_size )
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = random.sample( [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE], 1 )[0]
            blocksetleft1.append( ([ (x_start,y_start), (x_start,y_end), (x_end,y_end), (x_end,y_start) ], color ) )
            #blocksetleft2
            x_start = random.randrange( LEFT_MARGIN, CENTRE_COORDINATE_X - CENTRE_MARGIN - real_block_size )
            y_start = random.randrange( TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN - real_block_size )
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = random.sample( [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE], 1 )[0]
            blocksetleft2.append( ([ (x_start,y_start), (x_start,y_end), (x_end,y_end), (x_end,y_start) ], color ) )
            #blocksetright1
            x_start = random.randrange( CENTRE_COORDINATE_X + CENTRE_MARGIN, WINDOW_WIDTH - RIGHT_MARGIN - real_block_size )
            y_start = random.randrange( TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN - real_block_size )
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = random.sample( [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE], 1 )[0]
            blocksetright1.append( ([ (x_start,y_start), (x_start,y_end), (x_end,y_end), (x_end,y_start) ], color ) )
            #blocksetright2
            x_start = random.randrange( CENTRE_COORDINATE_X + CENTRE_MARGIN, WINDOW_WIDTH - RIGHT_MARGIN - real_block_size )
            y_start = random.randrange( TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN - real_block_size )
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = random.sample( [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE], 1 )[0]
            blocksetright2.append( ([ (x_start,y_start), (x_start,y_end), (x_end,y_end), (x_end,y_start) ], color ) )
        ###################
        
        for block, color in blocksetleft1:
            pygame.draw.polygon( screen, color, block, 0 )
        
        for block, color in blocksetright1:
            pygame.draw.polygon( screen, color, block, 0 )
        pygame.display.flip()            
        
        pygame.time.wait( STIMULUS_FLASH_TIME1 )
        clear()
        if not CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()  
        pygame.time.wait( WAIT4 )
        
        if same_or_different_flag == "same":
            if direction == "left":
                for block, color in blocksetleft1:
                    pygame.draw.polygon( screen, color, block, 0 )
                for block, color in blocksetright2:
                    pygame.draw.polygon( screen, color, block, 0 )
            elif direction == "right":
                for block, color in blocksetleft2:
                    pygame.draw.polygon( screen, color, block, 0 )
                for block, color in blocksetright1:
                    pygame.draw.polygon( screen, color, block, 0 )
        
        if same_or_different_flag == "different":
            for block, color in blocksetleft2:
                pygame.draw.polygon( screen, color, block, 0 )
            for block, color in blocksetright2:
                pygame.draw.polygon( screen, color, block, 0 )            

        pygame.display.flip()
        pygame.time.wait( STIMULUS_FLASH_TIME2 )
        clear()
        if not CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()
            
    #############################
    
    
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit( 0 )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)         

    def clear():
        screen.fill( BACKGROUND )
        pygame.display.update()
    
    def same_or_different( ):
        font = pygame.font.Font( None, 70 )
        text = font.render( "Same or different ('a' or 'l')", 1, BLACK )
        screen.blit( text, (CENTRE_COORDINATE_X-300, CENTRE_COORDINATE_Y-200) )
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                clear()
                return "same"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                clear()
                return "different"
            elif event.type == pygame.QUIT:
                sys.exit( 0 )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)     
            
    def space_to_continue():
        font = pygame.font.Font( None, 70 )
        text = font.render( "Press SPACE to continue or ESCAPE to exit", 1, BLACK )
        screen.blit( text, (CENTRE_COORDINATE_X-500, CENTRE_COORDINATE_Y-200) )
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                clear()
                return "space"
            elif event.type == pygame.QUIT:
                sys.exit( 0 )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)     
    
    pygame.init()
    if FULLSCREEN:
        possible_sizes = pygame.display.list_modes( 0, pygame.FULLSCREEN )
        global WINDOW_WIDTH
        global WINDOW_HEIGHT
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
    pygame.mouse.set_visible( False )
    space_to_continue()
    
    while True:
        handle_events()
        # # # # #
        #add hooks to handle events?
        
        s_or_d = random.sample( ("same", "different"), 1 )[0]
        l_or_r = random.sample( ( "left", "right" ), 1 )[0]       
        draw_cross()
        pygame.time.wait( WAIT1 )
        draw_cross()
        pygame.time.wait( WAIT2 )
        draw_arrow( l_or_r )
        pygame.time.wait( WAIT3 )
        draw_blocks( l_or_r, s_or_d )
        pygame.time.wait( WAIT5 )
        answer = same_or_different()  
        if answer == s_or_d:
            print "Correct"
        else:
            print "Incorrect"
        # # # # #
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()


