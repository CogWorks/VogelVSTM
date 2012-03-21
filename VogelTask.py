#!/usr/bin/env python -tt

#check this change


import sys
import random
import pygame
import vogelConfigurations as cnf


def main():

    ### pick random color
    def pick_random_color(notthis="none"):
        allavailable = [cnf.BLACK, cnf.WHITE, cnf.RED, cnf.GREEN, 
                        cnf.BLUE, cnf.YELLOW, cnf.PURPLE]
        # no color restriction
        if notthis=="none":
            color = random.sample(allavailable, 1)[0]
        # there is a color restriction
        else:
            listofnowavailablecolors = []
            for thecolor in allavailable:
                if thecolor == notthis:
                    pass
                else:
                    listofnowavailablecolors.append(thecolor)
            color = random.sample(listofnowavailablecolors, 1)[0]
        return color       
    
    ### draw fixation cross ###
    def draw_cross():
        pygame.draw.line( screen, cnf.CROSS_COLOR, (cnf.CENTRE_COORDINATE_X, 
                                                    cnf.CENTRE_COORDINATE_Y - cnf.CROSS_WIDTH * 
                                                    cnf.WINDOW_WIDTH), 
                                                   (cnf.CENTRE_COORDINATE_X,
                                                    cnf.CENTRE_COORDINATE_Y + 
                                                    cnf.CROSS_WIDTH * cnf.WINDOW_WIDTH), 
                                                    cnf.LINE_WIDTH)
        pygame.draw.line( screen, cnf.CROSS_COLOR, (cnf.CENTRE_COORDINATE_X-cnf.CROSS_WIDTH * 
                                                    cnf.WINDOW_WIDTH, cnf.CENTRE_COORDINATE_Y), 
                                                   (cnf.CENTRE_COORDINATE_X--cnf.CROSS_WIDTH*
                                                    cnf.WINDOW_WIDTH, cnf.CENTRE_COORDINATE_Y), 
                                                    cnf.LINE_WIDTH )
        pygame.display.flip()

    ### draw arrows ###
    def draw_arrow( direction ):
        if direction == "left":
            pygame.draw.polygon( screen, cnf.CROSS_COLOR, [ (cnf.CENTRE_COORDINATE_X - 40,
                                                             cnf.CENTRE_COORDINATE_Y - 70),
                                                            (cnf.CENTRE_COORDINATE_X - 40 + 15,
                                                             cnf.CENTRE_COORDINATE_Y - 70 + 5),
                                                            (cnf.CENTRE_COORDINATE_X - 40 + 15,
                                                             cnf.CENTRE_COORDINATE_Y - 70 - 5)], 
                                                              0 )  
            pygame.draw.line( screen, cnf.CROSS_COLOR, (cnf.CENTRE_COORDINATE_X-40, 
                                                         cnf.CENTRE_COORDINATE_Y-70),
                                                       (cnf.CENTRE_COORDINATE_X+40, 
                                                         cnf.CENTRE_COORDINATE_Y-70), 1)
        if direction == "right":
            pygame.draw.polygon(screen, cnf.CROSS_COLOR, [ (cnf.CENTRE_COORDINATE_X + 40,
                                                             cnf.CENTRE_COORDINATE_Y-70),
                                                            (cnf.CENTRE_COORDINATE_X + 40 - 15,
                                                             cnf.CENTRE_COORDINATE_Y - 70 + 5),
                                                            (cnf.CENTRE_COORDINATE_X + 40 - 15,
                                                             cnf.CENTRE_COORDINATE_Y - 70 - 5)],
                                                              0)  
            pygame.draw.line(screen, cnf.CROSS_COLOR, (cnf.CENTRE_COORDINATE_X-40, 
                                                       cnf.CENTRE_COORDINATE_Y-70),
                                                      (cnf.CENTRE_COORDINATE_X+40, 
                                                       cnf.CENTRE_COORDINATE_Y-70), 1)
        pygame.display.flip()
        pygame.time.wait(cnf.ARROW_FLASH_TIME)
        clear()
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()
    
    ### draw blocks ###
    def draw_blocks( direction, same_or_different_flag ):
    
        real_block_size = cnf.BLOCK_SIZE * cnf.WINDOW_WIDTH
        blocksetleft = []
        blocksetright = []

        for position in range(cnf.NUMBER_OF_BLOCKS):
            #blocksetleft
            x_start = random.randrange(cnf.LEFT_MARGIN, 
                                       cnf.CENTRE_COORDINATE_X-cnf.CENTRE_MARGIN-real_block_size)
            y_start = random.randrange(cnf.TOP_MARGIN, 
                                       cnf.WINDOW_HEIGHT-cnf.BOTTOM_MARGIN-real_block_size)
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = pick_random_color()
            blocksetleft.append(([ (x_start,y_start), (x_start,y_end), 
                                   (x_end,y_end), (x_end,y_start) ], color ))
            #blocksetright
            x_start = random.randrange(cnf.CENTRE_COORDINATE_X + cnf.CENTRE_MARGIN, 
                                       cnf.WINDOW_WIDTH - cnf.RIGHT_MARGIN - real_block_size)
            y_start = random.randrange(cnf.TOP_MARGIN, 
                                       cnf.WINDOW_HEIGHT - cnf.BOTTOM_MARGIN - real_block_size)
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = pick_random_color()
            blocksetright.append(([ (x_start,y_start), (x_start,y_end), 
                                      (x_end,y_end), (x_end,y_start) ], color ))
        
        #draw the blocks for the first flash
        for block, color in blocksetleft:
            pygame.draw.polygon(screen, color, block, 0)
        for block, color in blocksetright:
            pygame.draw.polygon(screen, color, block, 0)
        pygame.display.flip()            
        
        pygame.time.wait(cnf.STIMULUS_FLASH_TIME1)
        clear()
        
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross() 
         
        pygame.time.wait(cnf.WAIT4)
        
        #if the test (2nd) array is supposed to be the same
        if same_or_different_flag == "same":
            for block, color in blocksetleft:
                pygame.draw.polygon(screen, color, block, 0)
            for block, color in blocksetright:
                pygame.draw.polygon(screen, color, block, 0)
        
        #if the test (2nd) array is supposed to be different, carry on
        if same_or_different_flag == "different":
            change_index = random.randrange(0, cnf.NUMBER_OF_BLOCKS-1, 1)
            index = 0
            if direction == "left":
                for block, color in blocksetleft:
                    if index == change_index:
                        newcolor = pick_random_color(color)
                        pygame.draw.polygon(screen, newcolor, block, 0)
                    else:
                        pygame.draw.polygon(screen, color, block, 0)
                    index += 1
                for block, color in blocksetright:
                    pygame.draw.polygon(screen, color, block, 0)
            if direction == "right":
                for block, color in blocksetleft:
                    pygame.draw.polygon(screen, color, block, 0)
                for block, color in blocksetright:
                    if index == change_index:
                        newcolor = pick_random_color(color)
                        pygame.draw.polygon(screen, newcolor, block, 0)
                    else:
                        pygame.draw.polygon(screen, color, block, 0)
                    index += 1
                  
        pygame.display.flip()
        pygame.time.wait(cnf.STIMULUS_FLASH_TIME2)
        clear()
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()        
    #############################
    
    ### handle game events ###
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)         

    ### clear the screen ###
    def clear():
        screen.fill(cnf.BACKGROUND)
        pygame.display.update()
    
    ### ask subject if the blocks were the same, or different ###
    def same_or_different():
        font = pygame.font.Font(None, 70)
        text = font.render("Same or different ('a' or 'l')", 1, cnf.BLACK)
        screen.blit( text, (cnf.CENTRE_COORDINATE_X-300, cnf.CENTRE_COORDINATE_Y-200) )
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
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)     

    ### tell the subject to press SPACE to continue, before experiment starts ###     
    def space_to_continue():
        font = pygame.font.Font(None, 70)
        text = font.render("Press SPACE to continue or ESCAPE to exit", 1, cnf.BLACK)
        screen.blit(text, (cnf.CENTRE_COORDINATE_X-500, cnf.CENTRE_COORDINATE_Y-200))
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
    
    ### pygame goings-on ###
    pygame.init()
    if cnf.FULLSCREEN:
        possible_sizes = pygame.display.list_modes(0, pygame.FULLSCREEN)
        cnf.WINDOW_WIDTH = possible_sizes[0][0]
        cnf.WINDOW_HEIGHT = possible_sizes[0][1]
        screen = pygame.display.set_mode((cnf.WINDOW_WIDTH,cnf.WINDOW_HEIGHT),pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((cnf.WINDOW_WIDTH, cnf.WINDOW_HEIGHT))
    cnf.CENTRE_COORDINATE_X = cnf.WINDOW_WIDTH / 2
    cnf.CENTRE_COORDINATE_Y = cnf.WINDOW_HEIGHT / 2      
    pygame.display.set_caption(cnf.WINDOW_CAPTION)
    clock = pygame.time.Clock()
    screen.fill(cnf.BACKGROUND)
    pygame.mouse.set_visible(False)
    space_to_continue()
    
    ### MainLoop ###
    while True:
        handle_events()
        #add hooks to handle events?
        s_or_d = random.sample(("same", "different"), 1)[0]
        l_or_r = random.sample(("left", "right"), 1)[0]
        draw_cross()
        pygame.time.wait(cnf.WAIT1)
        draw_cross()
        pygame.time.wait(cnf.WAIT2)
        draw_arrow(l_or_r)
        pygame.time.wait(cnf.WAIT3)
        draw_blocks(l_or_r, s_or_d)
        pygame.time.wait(cnf.WAIT5)
        answer = same_or_different()  
        if answer == s_or_d:
            print "Correct"
        else:
            print "Incorrect"
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()


