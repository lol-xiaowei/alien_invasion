import pygame
# from rocket_move import MoveRocket


class Rocket:
    """火箭类"""
    def __init__(self, ai_game):
        # 获取屏幕资源
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 图片资源
        self.image = pygame.image.load('D:/86178/PycharmProject/alien_invasion/images/rocket.png').convert()
        self.rect = self.image.get_rect()

        # 自身属性
        self.rect.center = self.screen_rect.center
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update_pos(self):
        """根据标记更新自己的位置"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

    def blit_me(self):
        self.update_pos()
        self.screen.blit(self.image, self.rect)
