import sys
import pygame
from settings import Setting
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，创建游戏资源"""

        # init检查各个模块是否正常
        pygame.init()

        # 创建设置类实例
        self.settings = Setting()

        # 创建游戏资源
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵！")

        self.ship = Ship(self)

        # 设置颜色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘鼠标事件
            self._check_events()

            # 每次循环都重绘屏幕
            self._update_screen()

            # 延时
            pygame.time.delay(5)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            # 检测到点击×号退出程序
            if event.type == pygame.QUIT:
                sys.exit()

            # 检测到左右键移动飞船
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        """让最新绘制的屏幕可见"""
        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.update_pos()
        self.ship.blit_me()

        # 切换到新屏幕
        pygame.display.flip()


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
