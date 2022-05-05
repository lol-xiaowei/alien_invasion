import pygame.image


class Ship:
    """飞船类"""
    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""

        # 使飞船可以访问任意游戏资源
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        # 加载飞船图片和rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 设置飞船初始位置
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船的移动标记
        self.moving_right = False
        self.moving_left = False

        # 飞船的游戏属性
        self.x = float(self.rect.x)

    def blit_me(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        """移动飞船"""
        # 根据移动标志获取飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.setting.ship_speed
        # 根据self.x更新rect对象
        self.rect.x = self.x


