import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """显示得分"""
    def __init__(self, ai_game):
        """初始化"""
        self.ships = None
        self.aigame = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('arial', 36)

        # 显示初始得分图
        self.score_image = None
        self.score_rect = None
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        """将得分渲染成图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)
        # 屏幕右上角画得分（没显示）
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """渲染最高分为图像"""
        high_score = self.stats.high_score
        high_score_str = "highest score: " + str(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """检查是否最高分产生"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        """显示还剩多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.aigame)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)


