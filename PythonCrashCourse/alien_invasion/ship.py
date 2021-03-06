import pygame

class Ship():

    def __init__(self,ai_settings,screen):#screen指定了飞船要绘制到的位置，就是屏幕
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')#返回一个surface，用来表示飞船
        self.rect = self.image.get_rect() #获取飞船图形的矩形
        self.screen_rect = screen.get_rect()#获取屏幕的矩形

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)