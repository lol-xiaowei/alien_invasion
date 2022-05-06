import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，创建游戏资源"""

        # init检查各个模块是否正常
        pygame.init()

        # 创建设置类实例
        self.settings = Settings()

        # 创建屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 屏幕全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_height()
        # self.settings.screen_width = self.screen.get_width()

        # 设置标题
        pygame.display.set_caption("外星人入侵！")

        # 设置颜色
        self.bg_color = self.settings.bg_color

        # 创建飞船
        self.ship = Ship(self)

        # 创建子弹
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘鼠标事件
            self._check_events()
            # 更新飞船
            self._update_ship()
            # 更新子弹组
            self._update_bullets()
            # 每次循环都重绘屏幕
            self._update_screen()
            # 延时
            pygame.time.delay(2)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            # 检测到点击×号退出程序
            if event.type == pygame.QUIT:
                sys.exit()
            # 响应游戏内按键
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        # 飞船左右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 飞船开火
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开键"""
        # 飞船停止左右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # 按键Q退出游戏
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """让最新绘制的屏幕可见"""
        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)
        # 飞船图像行为
        self.ship.blit_me()
        # 子弹图像行为
        for bullet in self.bullets:
            bullet.draw_bullet()
        # 切换到新屏幕
        pygame.display.flip()

    def _update_ship(self):
        self.ship.update_pos()

    def _update_bullets(self):
        """对子弹组的内容做更新"""
        # 更新所有子弹位置
        self.bullets.update()
        # 消除消失的子弹(在副本中遍历，在数组中删除)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """向子弹组中加子弹"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
