import  pygame

class Rocket():

    def __init__(self,screen):
        self.screen = screen

        #加载火箭图片，获取火箭图片的矩形和屏幕的矩形
        self.image = pygame.image.load('image/feichuan.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #火箭的初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx

        #火箭的移动方向标志
        self.rocket_move_right = False
        self.rocket_move_left = False
        self.rocket_move_down = False
        self.rocket_move_up = False

        #火箭的移动速度
        self.rocket_move_speed = 2

    def rocket_update(self):
        #更新火箭的移动位置
        if self.rocket_move_down and self.rect.bottom <  self.screen_rect.bottom:
            self.rect.bottom += self.rocket_move_speed
        elif self.rocket_move_up and self.rect.top >  self.screen_rect.top:
            self.rect.bottom -= self.rocket_move_speed
        elif self.rocket_move_right and self.rect.centerx <  self.screen_rect.right:
            self.rect.centerx += self.rocket_move_speed
        elif self.rocket_move_left and self.rect.centerx >  self.screen_rect.left:
            self.rect.centerx -= self.rocket_move_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)