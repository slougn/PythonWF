import sys

import  pygame

from rocket import  Rocket
import game_function as gf

def run_game():
    #创建一个屏幕窗口
    pygame.init() #初始化背景设置
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Rocket Moving')

    my_rocket = Rocket(screen)
    # 设置背景颜色
    bg_color = (230,230,230)

    #开始游戏的主循环
    while True:
        gf.check_events(my_rocket)
        my_rocket.rocket_update()

        screen.fill(bg_color)
        my_rocket.blitme()
        pygame.display.flip()


run_game()
