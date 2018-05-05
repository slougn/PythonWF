"""这个文件中保存大量让游戏运行的函数"""
import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件 事件是用户玩游戏时执行的操作，如按键或移动鼠标
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:  # pygame.QUIT为用户单机游戏窗口的关闭按钮
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_envents(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_envents(event,ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    '''按键松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    """这是关于更新屏幕的代码，更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()  # 每次while循环都绘制一个空屏幕，并擦去旧屏幕，此语句为只有新屏幕可见