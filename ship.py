import pygame.image


class Ship:
    """飞船类"""
    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""

        # 使飞船可以访问任意游戏资源
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图片和rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 设置飞船初始位置
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船的移动标记
        self.moving_right = False
        self.moving_left = False

        # 飞船的游戏属性
        self.speed = 2

    def blit_me(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        """移动飞船"""
        # 左右移动
        if self.moving_right:
            self.rect.centerx += self.speed
        if self.moving_left:
            self.rect.centerx -= self.speed

        # 限制出屏幕
        if self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        elif self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left


