import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """控制外星人资源行为的类"""
    def __init__(self, ai_game):
        # Sprite初始化
        super().__init__()
        # 资源
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 属性
        self.settings = ai_game.settings
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 超级大坑！！！！！！
        #   self.speed = self.settings.alien_speed
        #   self.direction = self.settings.fleet_direction

        # 精确的x坐标
        self.x = float(self.rect.x)

    def update(self):
        """移动外星人"""
        # 超级大坑错误
        #   self.x += (self.speed * self.direction)
        #     因为主程序修改了setting对象，这里取值本来应该在主程序中的settings取瞬时值，
        #        但是这里把初始化时获得的配置值存到了自己的变量里面，所以fleet_direction不会变化！

        self.x += self.settings.alien_speed * (
            self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人在边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (
                self.rect.left <= screen_rect.left):
            return True

