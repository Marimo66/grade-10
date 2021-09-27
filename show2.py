# Emily Cheng's Room

import pygame
from pygame.locals import MOUSEBUTTONDOWN
import random

# colours
BLACK = (0, 0, 0)
GRAY = (100, 94, 94)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BUTTONRED = (184, 70, 71)
OFFRED = (103, 50, 43)
# wire colours
YELLOW = (189, 157, 43)
BLUE = (47, 80, 156)
PINK = (163, 31, 159)
RED = (163, 31, 24)

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Among one")

# images
pointer = pygame.image.load("pointer.png").convert_alpha()
firstbackground = pygame.image.load("background1.png").convert()
secondbackground = pygame.image.load("background2.png").convert()
character = pygame.image.load("character1.png").convert_alpha()
thirdbackground = pygame.image.load("background3.png").convert()
character_i = pygame.image.load("character2.png").convert_alpha()
thirdbackground_i = pygame.image.load("background3.5.png").convert()
fourthbackground = pygame.image.load("background4.png").convert()
lastbackground = pygame.image.load("background5.png").convert()

loading_i = pygame.image.load("loading.png").convert()
loading_ii = pygame.image.load("loading1.png").convert()
loading_iii = pygame.image.load("loading2.png").convert()
loading_iv = pygame.image.load("loading3.png").convert()


# door
def door():
    pygame.draw.rect(screen, GRAY, [570, 220 - door_animation, 80, 140])
    pygame.draw.rect(screen, GRAY, [570, 360 + door_animation, 80, 140])
    pygame.draw.rect(screen, BLACK, [570, 0, 80, 220])
    pygame.draw.rect(screen, BLACK, [570, 500, 80, 220])

door_animation = 0

# door button
button = pygame.Rect(650, 530, 30, 100)
# electrical button
electric_button = pygame.Rect(99, 256, 285, 145)
# yellow wire
yellow_wire = pygame.Rect(63, 76, 100, 70)
yellow_end = pygame.Rect(569, 542, 100, 70)
# blue wire
blue_wire = pygame.Rect(63, 226, 100, 70)
blue_end = pygame.Rect(569, 79, 100, 70)
# pink wire
pink_wire = pygame.Rect(63, 391, 100, 70)
pink_end = pygame.Rect(569, 390, 100, 70)
# red wire
red_wire = pygame.Rect(63, 531, 100, 70)
red_end = pygame.Rect(569, 229, 100, 70)


# speech bubble
def bubble():
    pygame.draw.rect(screen, WHITE, [bubble_x, bubble_y, 305, 170])


def instruction_one():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("There seems to be something", True, BLACK)
    screen.blit(text, [867, 165])
    text = font.render("wrong with the electricity.", True, BLACK)
    screen.blit(text, [867, 195])
    font = pygame.font.SysFont("Comic Sans", 23, False, False)
    text = font.render("Click anywhere to continue.", True, BLACK)
    screen.blit(text, [867, 239])


def instruction_two():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Click the red button to open", True, BLACK)
    screen.blit(text, [867, 180])
    text = font.render("the electricity room door", True, BLACK)
    screen.blit(text, [867, 205])


def firstdoor_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Uh oh! This door is locked!", True, BLACK)
    screen.blit(text, [895, 325])
    text = font.render("Looks like you will have to", True, BLACK)
    screen.blit(text, [895, 385])
    text = font.render("flip the switches to unlock it!", True, BLACK)
    screen.blit(text, [895, 415])


def seconddoor_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Nice! Door unlocked!", True, BLACK)
    screen.blit(text, [867, 150])


def thirdstage_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Now click the button to", True, BLACK)
    screen.blit(text, [667, 210])
    text = font.render("access the electrical.", True, BLACK)
    screen.blit(text, [667, 250])


def fourthstage_instruction():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Drag and drop the wires to", True, BLACK)
    screen.blit(text, [839, 300])
    text = font.render("fix the electricity.", True, BLACK)
    screen.blit(text, [839, 340])


def final_words():
    font = pygame.font.SysFont("Comic Sans", 30, False, False)
    text = font.render("Woohoo! We fixed the", True, BLACK)
    screen.blit(text, [839, 300])
    text = font.render("electricity!", True, BLACK)
    screen.blit(text, [839, 340])
    font = pygame.font.SysFont("Comic Sans", 23, False, False)
    text = font.render("Click anywhere to continue.", True, BLACK)
    screen.blit(text, [839, 380])

switch_i = 1
switch_ii = 2
switch_iii = 3
switch_iv = 4
switch_v = 5
switch_vi = 6

openswitch = [switch_i, switch_ii, switch_iii, switch_iv, switch_v, switch_vi]
choice_i = random.choice(openswitch)
openswitch.remove(choice_i)
choice_ii = random.choice(openswitch)
openswitch.remove(choice_ii)
choice_iii = random.choice(openswitch)

buttonoff_i = False
buttonoff_ii = False
buttonoff_iii = False
open_door = False

first_stage = 1
start_instruction = 1
second_stage = 0
door_instruction = 1
third_stage = 0
loading = True
timeloading = 0
fourthstage = 0
finish = 0

wire_draggingy = False
wire_draggingb = False
wire_draggingp = False
wire_draggingr = False
wire_complete = False

yellow_x = 107
yellow_y = 105

blue_x = 107
blue_y = 250

pink_x = 107
pink_y = 435

red_x = 107
red_y = 576

yellow = False
blue = False
pink = False
red = False
room = 1

clock = pygame.time.Clock()

level_complete = False

# -------- Main Program Loop -----------
while room == 1:
    pygame.mouse.set_visible(0)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:

            if first_stage == 1 and loading is False:
                start_instruction += 1

            if second_stage == 1:
                door_instruction += 1
            x, y = event.pos
            print(x, y)

            if button.collidepoint(x, y) and start_instruction > 2:
                second_stage = 1

            if button.collidepoint(x, y) and open_door is True:
                if third_stage == 0:
                    door_animation += 20

            if electric_button.collidepoint(x, y) and third_stage == 1 and loading is False:
                loading = True
                third_stage = 0
                fourthstage = 1

            if wire_complete is True:
                fourthstage = 0
                finish = 1

            if fourthstage == 1 and loading is False and event.button == 1:

                if yellow is False:
                    if yellow_wire.collidepoint(x,
                                                y) and wire_draggingp is False and wire_draggingb is False and wire_draggingr is False:
                        wire_draggingy = True
                    if yellow_end.collidepoint(yellow_x, yellow_y):
                        wire_draggingy = False
                        yellow = True

                if blue is False:
                    if blue_wire.collidepoint(x,
                                              y) and wire_draggingp is False and wire_draggingy is False and wire_draggingr is False:
                        wire_draggingb = True
                    if blue_end.collidepoint(blue_x, blue_y):
                        wire_draggingb = False
                        blue = True

                if pink is False:
                    if pink_wire.collidepoint(x,
                                              y) and wire_draggingy is False and wire_draggingb is False and wire_draggingr is False:
                        wire_draggingp = True
                    if pink_end.collidepoint(pink_x, pink_y):
                        wire_draggingp = False
                        pink = True

                if red is False:
                    if red_wire.collidepoint(x,
                                             y) and wire_draggingp is False and wire_draggingb is False and wire_draggingy is False:
                        wire_draggingr = True
                    if red_end.collidepoint(red_x, red_y):
                        wire_draggingr = False
                        red = True

    # game logic

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    if wire_draggingy is True:
        yellow_x = pygame.mouse.get_pos()[0]
        yellow_y = pygame.mouse.get_pos()[1]
    elif wire_draggingb is True:
        blue_x = pygame.mouse.get_pos()[0]
        blue_y = pygame.mouse.get_pos()[1]
    elif wire_draggingp is True:
        pink_x = pygame.mouse.get_pos()[0]
        pink_y = pygame.mouse.get_pos()[1]
    elif wire_draggingr is True:
        red_x = pygame.mouse.get_pos()[0]
        red_y = pygame.mouse.get_pos()[1]

    # --- Screen-clearing code goes here

    screen.fill(WHITE)

    if loading is True:
        for something in range(2):
            screen.blit(loading_i, [0, 0])
            timeloading += 1
            if timeloading > 10:
                screen.blit(loading_ii, [0, 0])
            if timeloading > 30:
                screen.blit(loading_iii, [0, 0])
            if timeloading > 50:
                screen.blit(loading_iv, [0, 0])
            if timeloading > 70:
                timeloading = 0
                if something == 1:
                    loading = False

    if first_stage == 1 and loading is False:
        screen.blit(firstbackground, [0, 0])
        screen.blit(character, [700, 300])
        door()
        pygame.draw.rect(screen, BUTTONRED, [650, 530, 30, 100])
        bubble_x = 857
        bubble_y = 120
        bubble()

        if start_instruction == 1:
            instruction_one()
        if start_instruction >= 2:
            instruction_two()
            if open_door is True:
                seconddoor_instruction()

    if second_stage == 1 and open_door is False:
        first_stage = 0
        screen.blit(secondbackground, [0, 0])
        bubble_x = 885
        bubble_y = 300
        bubble()
        if open_door is False and door_instruction >= 1:
            firstdoor_instruction()

        if choice_i == 1:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_i == 2:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_i == 3:
            button_i = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_i == 4:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_i == 5:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_i == 6:
            button_i = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if choice_ii == 1:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_ii == 2:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_ii == 3:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_ii == 4:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_ii == 5:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_ii == 6:
            button_ii = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if choice_iii == 1:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 132, 50, 99])
        elif choice_iii == 2:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 313, 50, 99])
        elif choice_iii == 3:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [404, 493, 50, 99])
        elif choice_iii == 4:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 131, 50, 99])
        elif choice_iii == 5:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 313, 50, 99])
        elif choice_iii == 6:
            button_iii = pygame.draw.rect(screen, BUTTONRED, [669, 493, 50, 99])

        if button_iii.collidepoint(x, y) and door_instruction > 1:
            choice_iii = 0
        if button_ii.collidepoint(x, y):
            choice_ii = 0
        if button_i.collidepoint(x, y):
            choice_i = 0

        if choice_i != 1 and choice_ii != 1 and choice_iii != 1:
            pygame.draw.rect(screen, OFFRED, [302, 132, 50, 99])
        if choice_i != 2 and choice_ii != 2 and choice_iii != 2:
            pygame.draw.rect(screen, OFFRED, [302, 313, 50, 99])
        if choice_i != 3 and choice_ii != 3 and choice_iii != 3:
            pygame.draw.rect(screen, OFFRED, [302, 493, 50, 99])
        if choice_i != 4 and choice_ii != 4 and choice_iii != 4:
            pygame.draw.rect(screen, OFFRED, [567, 131, 50, 99])
        if choice_i != 5 and choice_ii != 5 and choice_iii != 5:
            pygame.draw.rect(screen, OFFRED, [567, 313, 50, 99])
        if choice_i != 6 and choice_ii != 6 and choice_iii != 6:
            pygame.draw.rect(screen, OFFRED, [567, 493, 50, 99])

        if choice_i == 0 and choice_ii == 0 and choice_iii == 0:
            timeloading += 1
            if timeloading == 20:
                open_door = True
                first_stage = 1
                timeloading = 0

    if door_animation >= 140:
        second_stage = 0
        first_stage = 0
        third_stage = 1
        loading = True
        door_animation = 0

    # second part
    if third_stage == 1 and loading is False:
        screen.blit(thirdbackground, [0, 0])
        if 99 < pygame.mouse.get_pos()[0] < 370 and 256 < pygame.mouse.get_pos()[1] < 387:
            screen.blit(thirdbackground_i, [0, 0])
        bubble_x = 650
        bubble_y = 150
        bubble()
        thirdstage_instruction()
        screen.blit(character_i, [300, 250])

    if fourthstage == 1 and loading is False:
        screen.blit(fourthbackground, [0, 0])
        if wire_complete is True:
            screen.blit(lastbackground, [0, 0])
        bubble_x = 821
        bubble_y = 253
        bubble()
        if wire_complete is False:
            fourthstage_instruction()
        else:
            final_words()

        pygame.draw.line(screen, OFFRED, (643, 393), (643, 469), 20)
        pygame.draw.line(screen, OFFRED, (643, 229), (643, 304), 20)
        pygame.draw.line(screen, OFFRED, (643, 77), (643, 151), 20)

        if yellow is True:
            pygame.draw.line(screen, YELLOW, (107, 105), (601, 570), 45)
            pygame.draw.line(screen, GREEN, (643, 541), (643, 609), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 541), (643, 609), 20)
        if wire_draggingy is True:
            pygame.draw.line(screen, YELLOW, (107, 105), (yellow_x, yellow_y), 45)

        if blue is True:
            pygame.draw.line(screen, BLUE, (107, 265), (601, 109), 45)
            pygame.draw.line(screen, GREEN, (643, 77), (643, 151), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 77), (643, 151), 20)
        if wire_draggingb is True:
            pygame.draw.line(screen, BLUE, (107, 265), (blue_x, blue_y), 45)

        if pink is True:
            pygame.draw.line(screen, PINK, (107, 430), (601, 431), 45)
            pygame.draw.line(screen, GREEN, (643, 392), (643, 468), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 393), (643, 469), 20)
        if wire_draggingp is True:
            pygame.draw.line(screen, PINK, (107, 430), (pink_x, pink_y), 45)

        if red is True:
            pygame.draw.line(screen, RED, (107, 576), (601, 270), 45)
            pygame.draw.line(screen, GREEN, (643, 229), (643, 304), 20)
        else:
            pygame.draw.line(screen, OFFRED, (643, 229), (643, 304), 20)
        if wire_draggingr is True:
            pygame.draw.line(screen, RED, (107, 576), (red_x, red_y), 45)

        if red is True and blue is True and pink is True and yellow is True:
            timeloading += 1
            if timeloading == 20:
                wire_complete = True

    if finish == 1:
        room = 2

    screen.blit(pointer, [mouse_x - 26, mouse_y - 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

pygame.quit()
