#!/usr/bin/env python -tt

###########################################################
##                                                       ##
##   VogelTask.py   VogelVSTM.bbprojectd                 ##
##                                                       ##
##                Author: Tony Fischetti                 ##
##                        tony.fischetti                 ##
##                                                       ##
###########################################################

"""
More or less a clone of (Vogel et al., 2004) visual
short term memory task.

Uses Python 2.7 grammar
requires pygame module
requires pycogworks module (which requires PySide and PyCrypto)
"""

__author__ = 'Tony Fischetti'
__version__ = '1.1'

import sys
import random
import time
import pygame
import pycogworks
import vogelConfigurations as cnf


def main():
    ### pick random color ###
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
    
    ### collision detection ###
    def does_collide(pot_coord, restricted_coords):
        padding = cnf.BLOCK_SIZE * cnf.WINDOW_WIDTH + 5
        for item in restricted_coords:
            if (item[0] - padding) <= pot_coord[0] <= (item[0] + padding):
                if (item[1]-padding) <= pot_coord[1] <= (item[1] + padding):
                    return True
        return False
    
    ### random coordinates for left ###
    def random_coordinates_left():
        real_block_size = cnf.BLOCK_SIZE * cnf.WINDOW_WIDTH
        x_start = random.randrange(cnf.LEFT_MARGIN, 
                                   cnf.CENTRE_COORDINATE_X - 
                                   cnf.CENTRE_MARGIN - real_block_size)
        y_start = random.randrange(cnf.TOP_MARGIN, 
                                   cnf.WINDOW_HEIGHT - 
                                   cnf.BOTTOM_MARGIN - real_block_size)
        return x_start, y_start

    ### random coordinates for rightt ###
    def random_coordinates_right():
        real_block_size = cnf.BLOCK_SIZE * cnf.WINDOW_WIDTH
        x_start = random.randrange(cnf.CENTRE_COORDINATE_X + 
                                   cnf.CENTRE_MARGIN, 
                                   cnf.WINDOW_WIDTH - cnf.RIGHT_MARGIN - 
                                   real_block_size)
        y_start = random.randrange(cnf.TOP_MARGIN, 
                                   cnf.WINDOW_HEIGHT - cnf.BOTTOM_MARGIN - 
                                   real_block_size)
        return x_start, y_start
    
    ### draw fixation cross ###
    def draw_cross():
        pygame.draw.line( screen, cnf.CROSS_COLOR, 
                                 (cnf.CENTRE_COORDINATE_X, 
                                  cnf.CENTRE_COORDINATE_Y - cnf.CROSS_WIDTH * 
                                  cnf.WINDOW_WIDTH), 
                                 (cnf.CENTRE_COORDINATE_X,
                                  cnf.CENTRE_COORDINATE_Y + 
                                  cnf.CROSS_WIDTH * cnf.WINDOW_WIDTH), 
                                  cnf.LINE_WIDTH)
        pygame.draw.line( screen, cnf.CROSS_COLOR, 
                                  (cnf.CENTRE_COORDINATE_X - cnf.CROSS_WIDTH * 
                                   cnf.WINDOW_WIDTH, cnf.CENTRE_COORDINATE_Y), 
                                  (cnf.CENTRE_COORDINATE_X + cnf.CROSS_WIDTH *
                                   cnf.WINDOW_WIDTH, cnf.CENTRE_COORDINATE_Y), 
                                   cnf.LINE_WIDTH )
        pygame.display.flip()

    ### draw arrows ###
    def draw_arrow( direction ):
        if direction == "left":
            pygame.draw.polygon( screen, cnf.CROSS_COLOR, 
                                      [ (cnf.CENTRE_COORDINATE_X - 40,
                                         cnf.CENTRE_COORDINATE_Y - 70),
                                        (cnf.CENTRE_COORDINATE_X - 40 + 15,
                                         cnf.CENTRE_COORDINATE_Y - 70 + 5),
                                        (cnf.CENTRE_COORDINATE_X - 40 + 15,
                                         cnf.CENTRE_COORDINATE_Y - 70 - 5)], 0)  
            pygame.draw.line( screen, cnf.CROSS_COLOR, 
                                     (cnf.CENTRE_COORDINATE_X - 40, 
                                      cnf.CENTRE_COORDINATE_Y - 70),
                                     (cnf.CENTRE_COORDINATE_X + 40, 
                                      cnf.CENTRE_COORDINATE_Y - 70), 1)
        if direction == "right":
            pygame.draw.polygon(screen, cnf.CROSS_COLOR, 
                                     [ (cnf.CENTRE_COORDINATE_X + 40,
                                        cnf.CENTRE_COORDINATE_Y - 70),
                                       (cnf.CENTRE_COORDINATE_X + 40 - 15,
                                        cnf.CENTRE_COORDINATE_Y - 70 + 5),
                                        (cnf.CENTRE_COORDINATE_X + 40 - 15,
                                        cnf.CENTRE_COORDINATE_Y - 70 - 5)], 0)  
            pygame.draw.line(screen, cnf.CROSS_COLOR, 
                                    (cnf.CENTRE_COORDINATE_X - 40, 
                                     cnf.CENTRE_COORDINATE_Y - 70),
                                    (cnf.CENTRE_COORDINATE_X + 40, 
                                     cnf.CENTRE_COORDINATE_Y - 70), 1)
        pygame.display.flip()
        pygame.time.wait(cnf.ARROW_FLASH_TIME)
        clear()
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()
    
    ### draw blocks ###
    def draw_blocks( direction, same_or_different_flag ):
        ret_list = []
        real_block_size = cnf.BLOCK_SIZE * cnf.WINDOW_WIDTH
        blocksetleft = []
        blocksetright = []
        restricted_coords_left = []
        restricted_coords_right = []
        for position in range(cnf.NUMBER_OF_BLOCKS):
            #blocksetleft
            x_start, y_start = random_coordinates_left()
            if does_collide((x_start,y_start), restricted_coords_left):
                x_start, y_start = random_coordinates_left()
                if does_collide((x_start,y_start), restricted_coords_left):
                    x_start, y_start = random_coordinates_left()
                    if does_collide((x_start,y_start), restricted_coords_left):
                        x_start, y_start = random_coordinates_left()
            restricted_coords_left.append((x_start,y_start))
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = pick_random_color()
            blocksetleft.append(([ (x_start,y_start), (x_start,y_end), 
                                   (x_end,y_end), (x_end,y_start) ], color))
            #blocksetright
            x_start, y_start = random_coordinates_right()
            if does_collide((x_start,y_start), restricted_coords_right):
                x_start, y_start = random_coordinates_right()
                if does_collide((x_start,y_start), restricted_coords_right):
                    x_start, y_start = random_coordinates_right()
                    if does_collide((x_start,y_start), restricted_coords_right):
                        x_start, y_start = random_coordinates_right()
            restricted_coords_right.append((x_start,y_start))
            x_end = x_start + real_block_size
            y_end = y_start + real_block_size
            color = pick_random_color()
            blocksetright.append(([ (x_start,y_start), (x_start,y_end), 
                                      (x_end,y_end), (x_end,y_start) ], color))
        #draw the blocks for the first flash
        for block, color in blocksetleft:
            pygame.draw.polygon(screen, color, block, 0)
        for block, color in blocksetright:
            pygame.draw.polygon(screen, color, block, 0)
        ret_list.append(blocksetleft)
        ret_list.append(blocksetright)
        pygame.display.flip()            
        pygame.time.wait(cnf.STIMULUS_FLASH_TIME1)
        clear()
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross() 
        pygame.time.wait(cnf.WAIT4)
        #if the test (2nd) array is supposed to be the same
        if same_or_different_flag == "same":
            ret_list.append("NA")
            ret_list.append("NA")
            ret_list.append("NA")
            for block, color in blocksetleft:
                pygame.draw.polygon(screen, color, block, 0)
            for block, color in blocksetright:
                pygame.draw.polygon(screen, color, block, 0)
        #if the test (2nd) array is supposed to be different, carry on
        if same_or_different_flag == "different":
            change_index = random.randrange(0, cnf.NUMBER_OF_BLOCKS-1, 1)
            ret_list.append(change_index)
            index = 0
            if direction == "left":
                for block, color in blocksetleft:
                    if index == change_index:
                        newcolor = pick_random_color(color)
                        ret_list.append(color)
                        ret_list.append(newcolor)
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
                        ret_list.append(color)
                        ret_list.append(newcolor)
                        pygame.draw.polygon(screen, newcolor, block, 0)
                    else:
                        pygame.draw.polygon(screen, color, block, 0)
                    index += 1
        pygame.display.flip()
        pygame.time.wait(cnf.STIMULUS_FLASH_TIME2)
        clear()
        if not cnf.CROSS_DISAPPEARS_ON_ARROW:
            draw_cross()       
        return ret_list
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
        screen.blit(text, (cnf.CENTRE_COORDINATE_X-300, 
                           cnf.CENTRE_COORDINATE_Y-200))
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

    # tell the subject to press SPACE to continue, before experiment starts #     
    def space_to_continue(message="Press SPACE to continue or ESCAPE to exit"):
        font = pygame.font.Font(None, 70)
        text = font.render(message, 1, cnf.BLACK)
        screen.blit(text, (cnf.CENTRE_COORDINATE_X-500,  
                           cnf.CENTRE_COORDINATE_Y-200))
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
    
    user_dict = pycogworks.getSubjectInfo()
    pycogworks.writeHistoryFile(cnf.historyfilename, {"rin": user_dict["rin"]})
    ### pygame goings-on ###
    pygame.init()
    logfile = open(cnf.logfilename, "a")
    headers = "trial_number,leftorright,sameordiff,"
    headers += "subjanswer,correct?,trialtime,cumulative_time,"
    headers += "leftblocks,rightblocks,blockchanged,oldcolor,newcolor\n"
    logfile.write(headers)
    if cnf.FULLSCREEN:
        possible_sizes = pygame.display.list_modes(0, pygame.FULLSCREEN)
        cnf.WINDOW_WIDTH = possible_sizes[0][0]
        cnf.WINDOW_HEIGHT = possible_sizes[0][1]
        screen = pygame.display.set_mode((cnf.WINDOW_WIDTH,cnf.WINDOW_HEIGHT),
                                          pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((cnf.WINDOW_WIDTH, cnf.WINDOW_HEIGHT))
    cnf.CENTRE_COORDINATE_X = cnf.WINDOW_WIDTH / 2
    cnf.CENTRE_COORDINATE_Y = cnf.WINDOW_HEIGHT / 2      
    pygame.display.set_caption(cnf.WINDOW_CAPTION)
    clock = pygame.time.Clock()
    screen.fill(cnf.BACKGROUND)
    pygame.mouse.set_visible(False)
    space_to_continue()
    start_time = time.time()
    previous_time = start_time
    trial_number = 0
    
    ### MainLoop ###
    while True:
        if trial_number >= cnf.NUM_OF_TRIALS:
            space_to_continue("Thank you for your participation!")    
        handle_events()
        s_or_d = random.sample(("same", "different"), 1)[0]
        l_or_r = random.sample(("left", "right"), 1)[0]
        draw_cross()
        pygame.time.wait(cnf.WAIT1)
        draw_cross()
        pygame.time.wait(cnf.WAIT2)
        draw_arrow(l_or_r)
        pygame.time.wait(cnf.WAIT3)
        draw_info = draw_blocks(l_or_r, s_or_d)
        pygame.time.wait(cnf.WAIT5)
        trial_number += 1
        answer = same_or_different()
        cumulative_time = pycogworks.get_time() - start_time
        if trial_number == 1:
            this_trial_time = cumulative_time
        else:
            this_trial_time = cumulative_time - previous_time
        previous_time = cumulative_time
        if answer == s_or_d:
            isCorrect = "Correct"
        else:
            isCorrect = "Incorrect"
        logline = ",".join([ str(trial_number), l_or_r, s_or_d, str(answer), 
                             isCorrect, str(this_trial_time), 
                             str(cumulative_time), 
                             str(draw_info[0]).replace(",", ":"),
                             str(draw_info[1]).replace(",", ":"), 
                             str(draw_info[2]),
                             str(draw_info[3]).replace(",", ":"), 
                             str(draw_info[4]).replace(",", ":")])
        logline += "\n"
        logfile.write(logline)
        pygame.display.flip()
    logfile.close()
    pygame.quit()

if __name__ == "__main__":
    main()


