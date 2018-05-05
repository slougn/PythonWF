import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init() #初始化背景设置，让pygame能够正确工作
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #创建一个名为screen的现实窗口，制定窗口的尺寸,参数为一个元组
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #设置背景色
    #bg_color = (230,230,230)

    #开始游戏的主循环
    while True:#循环侦听循环
        gf.check_events(ship)#检测事件
        ship.update()
        gf.update_screen(ai_settings,screen,ship)#每次循环时都重绘屏幕


run_game()#初始化游戏并开始循环