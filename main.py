from multiprocessing.connection import wait
import pygame, sys
from pygame.locals import *
import random, time
import os
import keyboard
from 吃饭D1 import *
from 学校生活D1 import *
from 学校生活D2 import *
from 语法 import*
import msvcrt as m
import keyboard

def wait():
    m.getch()
 
#Initializing 
pygame.init()
pygame.event.pump()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
RED   = (255, 0, 0)
ORANGE = (255, 100, 20)
YELLOW = (240, 240, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (100, 1, 200)
PINK = (255, 0, 200)
BROWN = (100, 80, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FIRE = (255, 80, 10)
BOOGER = (200, 255, 0)
AQUA = (0, 255, 220)
INDIGO = (70, 0, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650

font = pygame.font.Font("中文jeopardy\simsun\SIMSUN.ttf", 40)
font_small = pygame.font.Font("中文jeopardy\simsun\SIMSUN.ttf", 20)
font_medium = pygame.font.Font("中文jeopardy\simsun\SIMSUN.ttf", 50)
font_large = pygame.font.Font("中文jeopardy\simsun\SIMSUN.ttf", 70)
pygame.font.init()

DISPLAYSURF = pygame.display.set_mode((1200,650))
DISPLAYSURF.fill(INDIGO)#background
pygame.display.set_caption("中文 JEOPARDY!")

第一组 = 0
第二组 = 0
category_list = ["吃饭D1", "学校生活D1", "学校生活D2", "语法"]
points_list = [100,200,300,400,500]
buttons_list = ["吃饭D1 100","吃饭D1 200","吃饭D1 300","吃饭D1 400","吃饭D1 500","学校生活D1 100","学校生活D1 200","学校生活D1 300","学校生活D1 400","学校生活D1 500","学校生活D2 100","学校生活D2 200","学校生活D2 300","学校生活D2 400","学校生活D2 500","语法 100","语法 200","语法 300","语法 400","语法 500"]

y_category_start = 0
y_100_start = 108.33
y_200_start = 216.66
y_300_start = 324.99
y_400_start = 433.32
y_500_start = 541.65

x_吃饭D1_start = 0
x_学校生活D1_start = 300
x_学校生活D2_start = 600
x_语法_start = 900

def Question(question):
    time.sleep(1)
    DISPLAYSURF.fill(INDIGO)
    question_choice = font_medium.render(str(question), True, WHITE)
    question_rect = question_choice.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    DISPLAYSURF.blit(question_choice, question_rect)
    pygame.display.update()
    FramePerSec.tick(FPS)
    time.sleep(1)
    
    # for i in range(10):
    #     pygame.draw.rect(DISPLAYSURF,INDIGO,(0,0,100,100))
    #     count = font.render(str(i+1),True, WHITE)
    #     DISPLAYSURF.blit(count, (2,2))
    #     # time.sleep(1)
    #     pygame.display.update()
    #     FramePerSec.tick(FPS)

    die = False
    while not die:
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    die = True

def Answer(answer):
    DISPLAYSURF.fill(INDIGO)
    answer_to_print = font_medium.render(str(answer), True, WHITE)
    answer_rect = answer_to_print.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    DISPLAYSURF.blit(answer_to_print, answer_rect)
    pygame.display.update()
    FramePerSec.tick(FPS)

    die = False
    while not die:
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    die = True
   
            



while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
       

        #category boxes
        pygame.draw.rect(DISPLAYSURF,BLUE,(0,0,1200,y_100_start))

        category1 = font.render(str(category_list[0]), True, WHITE)
        DISPLAYSURF.blit(category1, (x_吃饭D1_start+75,y_category_start+30))

        category2 = font.render(str(category_list[1]), True, WHITE)
        DISPLAYSURF.blit(category2, (x_学校生活D1_start+50,y_category_start+30))

        category3 = font.render(str(category_list[2]), True, WHITE)
        DISPLAYSURF.blit(category3, (x_学校生活D2_start+50,y_category_start+30))

        category4 = font.render(str(category_list[3]), True, WHITE)
        DISPLAYSURF.blit(category4, (x_语法_start+100,y_category_start+30))

        #point boxes
        chi_100 = font.render(str(buttons_list[0]), True, WHITE)
        DISPLAYSURF.blit(chi_100, (x_吃饭D1_start+40,y_100_start+30))
        chi_200 = font.render(str(buttons_list[1]), True, WHITE)
        DISPLAYSURF.blit(chi_200, (x_吃饭D1_start+40,y_200_start+30))
        chi_300 = font.render(str(buttons_list[2]), True, WHITE)
        DISPLAYSURF.blit(chi_300, (x_吃饭D1_start+40,y_300_start+30))
        chi_400 = font.render(str(buttons_list[3]), True, WHITE)
        DISPLAYSURF.blit(chi_400, (x_吃饭D1_start+40,y_400_start+30))
        chi_500 = font.render(str(buttons_list[4]), True, WHITE)
        DISPLAYSURF.blit(chi_500, (x_吃饭D1_start+40,y_500_start+30))

        xue1_100 = font.render(str(buttons_list[5]), True, WHITE)
        DISPLAYSURF.blit(xue1_100, (x_学校生活D1_start+15,y_100_start+30))
        xue1_200 = font.render(str(buttons_list[6]), True, WHITE)
        DISPLAYSURF.blit(xue1_200, (x_学校生活D1_start+15,y_200_start+30))
        xue1_300 = font.render(str(buttons_list[7]), True, WHITE)
        DISPLAYSURF.blit(xue1_300, (x_学校生活D1_start+15,y_300_start+30))
        xue1_400 = font.render(str(buttons_list[8]), True, WHITE)
        DISPLAYSURF.blit(xue1_400, (x_学校生活D1_start+15,y_400_start+30))
        xue1_500 = font.render(str(buttons_list[9]), True, WHITE)
        DISPLAYSURF.blit(xue1_500, (x_学校生活D1_start+15,y_500_start+30))

        xue2_100 = font.render(str(buttons_list[10]), True, WHITE)
        DISPLAYSURF.blit(xue2_100, (x_学校生活D2_start+15,y_100_start+30))
        xue2_200 = font.render(str(buttons_list[11]), True, WHITE)
        DISPLAYSURF.blit(xue2_200, (x_学校生活D2_start+15,y_200_start+30))
        xue2_300 = font.render(str(buttons_list[12]), True, WHITE)
        DISPLAYSURF.blit(xue2_300, (x_学校生活D2_start+15,y_300_start+30))
        xue2_400 = font.render(str(buttons_list[13]), True, WHITE)
        DISPLAYSURF.blit(xue2_400, (x_学校生活D2_start+15,y_400_start+30))
        xue2_500 = font.render(str(buttons_list[14]), True, WHITE)
        DISPLAYSURF.blit(xue2_500, (x_学校生活D2_start+15,y_500_start+30))

        yu_100 = font.render(str(buttons_list[15]), True, WHITE)
        DISPLAYSURF.blit(yu_100, (x_语法_start+50,y_100_start+30))
        yu_200 = font.render(str(buttons_list[16]), True, WHITE)
        DISPLAYSURF.blit(yu_200, (x_语法_start+50,y_200_start+30))
        yu_300 = font.render(str(buttons_list[17]), True, WHITE)
        DISPLAYSURF.blit(yu_300, (x_语法_start+50,y_300_start+30))
        yu_400 = font.render(str(buttons_list[18]), True, WHITE)
        DISPLAYSURF.blit(yu_400, (x_语法_start+50,y_400_start+30))
        yu_500 = font.render(str(buttons_list[19]), True, WHITE)
        DISPLAYSURF.blit(yu_500, (x_语法_start+50,y_500_start+30))

        #team scores

        #lines so it looks better- inbetween each column
        pygame.draw.line(DISPLAYSURF, WHITE, (x_学校生活D1_start, y_category_start), (x_学校生活D1_start,SCREEN_HEIGHT), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_学校生活D2_start, y_category_start), (x_学校生活D2_start,SCREEN_HEIGHT), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_语法_start+30, y_category_start), (x_语法_start+30,SCREEN_HEIGHT), width=1)
        #lines so it looks better- inbetween rows
        pygame.draw.line(DISPLAYSURF, WHITE, (x_吃饭D1_start, y_100_start), (SCREEN_WIDTH, y_100_start), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_吃饭D1_start, y_200_start), (SCREEN_WIDTH, y_200_start), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_吃饭D1_start, y_300_start), (SCREEN_WIDTH, y_300_start), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_吃饭D1_start, y_400_start), (SCREEN_WIDTH, y_400_start), width=1)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_吃饭D1_start, y_500_start), (SCREEN_WIDTH, y_500_start), width=1)

        #if its pressed down- random and remove it
        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            #chi fan mouse boxes
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_100_start <= mouse[1] <= y_200_start:
                chifan_100_random = random.choice(list(dict_100_chifan.items()))
                question = chifan_100_random[0]
                answer = chifan_100_random[1]
                Question(question)
                
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("吃饭D1 100")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_200_start <= mouse[1] <= y_300_start:
                chifan_200_random = random.choice(list(dict_200_chifan.items()))
                question = chifan_200_random[0]
                answer = chifan_200_random[1]
                Question(question)
                # # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("吃饭D1 200")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_300_start <= mouse[1] <= y_400_start:
                chifan_300_random = random.choice(list(dict_300_chifan.items()))
                question = chifan_300_random[0]
                answer = chifan_300_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("吃饭D1 300")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_400_start <= mouse[1] <= y_500_start:
                chifan_400_random = random.choice(list(dict_400_chifan.items()))
                question = chifan_400_random[0]
                answer = chifan_400_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("吃饭D1 400")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_500_start <= mouse[1] <= SCREEN_HEIGHT:
                chifan_500_random = random.choice(list(dict_500_chifan.items()))
                question = chifan_500_random[0]
                answer = chifan_500_random[1]
                Question(question)
                pygame.display.update()
                # keyboard.wait('space')               
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("吃饭D1 500")
                except ValueError:
                    continue 
                else:
                    buttons_list[x] = "不可以"
                    continue

            #xuexiao D1 mouse boxes
            if x_学校生活D1_start <= mouse[0] <= x_学校生活D2_start and y_100_start <= mouse[1] <= y_200_start:
                xuexiao1_100_random = random.choice(list(dict_100_xuexiao1.items()))
                question = xuexiao1_100_random[0]
                answer = xuexiao1_100_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("学校生活D1 100")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_学校生活D1_start <= mouse[0] <= x_学校生活D2_start and y_200_start <= mouse[1] <= y_300_start:
                xuexiao1_200_random = random.choice(list(dict_200_xuexiao1.items()))
                question = xuexiao1_200_random[0]
                answer = xuexiao1_200_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                try:
                    x = buttons_list.index("学校生活D1 200")
                except ValueError:
                    continue
                else:
                    buttons_list[x] = "不可以"
                    continue
            if x_学校生活D1_start <= mouse[0] <= x_学校生活D2_start and y_300_start <= mouse[1] <= y_400_start:
                xuexiao1_300_random = random.choice(list(dict_300_xuexiao1.items()))
                question = xuexiao1_300_random[0]
                answer = xuexiao1_300_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D1 300")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D1_start <= mouse[0] <= x_学校生活D2_start and y_400_start <= mouse[1] <= y_500_start:
                xuexiao1_400_random = random.choice(list(dict_400_xuexiao1.items()))
                question = xuexiao1_400_random[0]
                answer = xuexiao1_400_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D1 400")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D1_start <= mouse[0] <= x_学校生活D2_start and y_500_start <= mouse[1] <= SCREEN_HEIGHT:
                xuexiao1_500_random = random.choice(list(dict_500_xuexiao1.items()))
                question = xuexiao1_500_random[0]
                answer = xuexiao1_500_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D1 500")
                buttons_list[x] = "不可以"
                continue

            #xuexiao D2 mouse boxes
            if x_学校生活D2_start <= mouse[0] <= x_语法_start and y_100_start <= mouse[1] <= y_200_start:
                xuexiao2_100_random = random.choice(list(dict_100_xuexiao2.items()))
                question = xuexiao2_100_random[0]
                answer = xuexiao2_100_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D2 100")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D2_start <= mouse[0] <= x_语法_start and y_200_start <= mouse[1] <= y_300_start:
                xuexiao2_200_random = random.choice(list(dict_200_xuexiao2.items()))
                question = xuexiao2_200_random[0]
                answer = xuexiao2_200_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D2 200")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D2_start <= mouse[0] <= x_语法_start and y_300_start <= mouse[1] <= y_400_start:
                xuexiao2_300_random = random.choice(list(dict_300_xuexiao2.items()))
                question = xuexiao2_300_random[0]
                answer = xuexiao2_300_random[1]
                Question(question)
                # keyboard.wait('space')                
                Answer(answer)
                # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D2 300")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D2_start <= mouse[0] <= x_语法_start and y_400_start <= mouse[1] <= y_500_start:
                xuexiao2_400_random = random.choice(list(dict_400_xuexiao2.items()))
                question = xuexiao2_400_random[0]
                answer = xuexiao2_400_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D2 400")
                buttons_list[x] = "不可以"
                continue
            if x_学校生活D2_start <= mouse[0] <= x_语法_start and y_500_start <= mouse[1] <= SCREEN_HEIGHT:
                xuexiao2_500_random = random.choice(list(dict_500_xuexiao2.items()))
                question = xuexiao2_500_random[0]
                answer = xuexiao2_500_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("学校生活D2 500")
                buttons_list[x] = "不可以"
                continue

            #yufa mouse boxes
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_100_start <= mouse[1] <= y_200_start:
                yufa_100_random = random.choice(list(dict_100_yufa.items()))
                question = yufa_100_random[0]
                answer = yufa_100_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("语法 100")
                buttons_list[x] = "不可以"
                continue
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_200_start <= mouse[1] <= y_300_start:
                yufa_200_random = random.choice(list(dict_200_yufa.items()))
                question = yufa_200_random[0]
                answer = yufa_200_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("语法 200")
                buttons_list[x] = "不可以"
                continue
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_300_start <= mouse[1] <= y_400_start:
                yufa_300_random = random.choice(list(dict_300_yufa.items()))
                question = yufa_300_random[0]
                answer = yufa_300_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("语法 300")
                buttons_list[x] = "不可以"
                continue
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_400_start <= mouse[1] <= y_500_start:
                yufa_400_random = random.choice(list(dict_400_yufa.items()))
                question = yufa_400_random[0]
                answer = yufa_400_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("语法 400")
                buttons_list[x] = "不可以"
                continue
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_500_start <= mouse[1] <= SCREEN_HEIGHT:
                yufa_500_random = random.choice(list(dict_500_yufa.items()))
                question = yufa_500_random[0]
                answer = yufa_500_random[1]
                Question(question)
                # # keyboard.wait('space')                
                Answer(answer)
                # # keyboard.wait('space')
                DISPLAYSURF.fill(INDIGO)
                x = buttons_list.index("语法 500")
                buttons_list[x] = "不可以"
                continue


            #categories
            if x_吃饭D1_start <= mouse[0] <= x_学校生活D1_start and y_category_start <= mouse[1] <= y_100_start:
                chifan_image = pygame.image.load(r'中文jeopardy\chifan.jpg')
                chifan_words = pygame.image.load(r'中文jeopardy\chifan words.PNG')
                chifan_image = pygame.transform.scale(chifan_image, (300,300))
                time.sleep(1)
                DISPLAYSURF.fill(BLUE)
                image_rect = chifan_image.get_rect(center =(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-150))
                words_rect = chifan_words.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150))
                DISPLAYSURF.blit(chifan_image, image_rect)
                DISPLAYSURF.blit(chifan_words, words_rect)
                pygame.display.update()
                FramePerSec.tick(FPS)
                # # keyboard.wait('space')
                die = False
                while not die:
                    pygame.display.flip()
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_SPACE:
                                die = True
                DISPLAYSURF.fill(INDIGO)
                continue

            
            if x_学校生活D1_start <= mouse[0] <= x_语法_start and y_category_start <= mouse[1] <= y_100_start:
                xuexiaoshenghuo_image = pygame.image.load(r'中文jeopardy\xuexiaoshenghuo.jpg')
                xuexiaoshenghuo_words = pygame.image.load(r'中文jeopardy\XUEXIAOwords.PNG')
                xuexiaoshenghuo_image = pygame.transform.scale(xuexiaoshenghuo_image, (300,300))
                time.sleep(1)
                DISPLAYSURF.fill(BLUE)
                image_rect = xuexiaoshenghuo_image.get_rect(center =(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-150))
                words_rect = xuexiaoshenghuo_words.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150))
                DISPLAYSURF.blit(xuexiaoshenghuo_image, image_rect)
                DISPLAYSURF.blit(xuexiaoshenghuo_words, words_rect)
                pygame.display.update()
                FramePerSec.tick(FPS)
                # # keyboard.wait('space')
                die = False
                while not die:
                    pygame.display.flip()
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_SPACE:
                                die = True
                DISPLAYSURF.fill(INDIGO)
                continue

            yufa_words = pygame.image.load(r'中文jeopardy\yufawords.PNG')
            if x_语法_start <= mouse[0] <= SCREEN_WIDTH and y_category_start <= mouse[1] <= y_100_start:
                yufa_words = pygame.image.load(r'中文jeopardy\yufawords.PNG')
                time.sleep(1)
                DISPLAYSURF.fill(BLUE)
                words_rect = yufa_words.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                DISPLAYSURF.blit(yufa_words, words_rect)
                pygame.display.update()
                FramePerSec.tick(FPS)
                # # keyboard.wait('space')
                die = False
                while not die:
                    pygame.display.flip()
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN:
                            if ev.key == pygame.K_SPACE:
                                die = True
                DISPLAYSURF.fill(INDIGO)
                continue

    pygame.display.update()
    FramePerSec.tick(FPS)