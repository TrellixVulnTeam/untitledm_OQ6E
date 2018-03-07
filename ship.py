import pygame


class Ship():
    def __init__(self,ai_settings,screen):
        #初始化飞船
        self.screen=screen
        self.ai_settings=ai_settings

        #获取飞船图像和其属性
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)

        #移动标记
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标记调整飞船的位置"""
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor

        #更据self.center更新rect对象
        self.rect.centerx=self.center


    def blitme(self):
        #将飞船绘制出来
        self.screen.blit(self.image,self.rect)