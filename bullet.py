import pygame
import settings


class Bullet:
    """描述子弹的类"""
    def __init__(self, ai_game):
        # 访问游戏资源
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings.Settings()

        # 构建自身图像和矩形
        self.image = pygame.Surface(size=(self.settings.bullet_width, self.settings.bullet_height))
        self.image.fill(self.settings.bullet_color)
        self.rect = self.image.get_rect()

        # 子弹自身属性
        self.speed = self.settings.bullet_speed
        self.rect.center = ai_game.ship.rect.center

    def update_pos(self):
        self.rect.y -= self.speed

    def blit_me(self):
        """绘制子弹"""
        self.screen.blit(self.image, self.rect)



