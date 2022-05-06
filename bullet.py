import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射子弹的类"""

    def __init__(self, ai_game):
        """管理飞船发射子弹的类"""
        # 继承父类
        super().__init__()
        # 游戏资源
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 自身属性
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed
        # 矩形位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # 为小数做准备
        self.y = float(self.rect.y)

    def update(self):
        """子弹向上飞"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

