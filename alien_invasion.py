import sys
from time import sleep

import pygame

from settings import Settings
from gm_stats import GmStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import  Scoreboard


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，创建游戏资源"""

        # init检查各个模块是否正常
        pygame.init()

        # 创建设置类实例
        self.settings = Settings()

        # 创建屏幕
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # 屏幕全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_height()
        # self.settings.screen_width = self.screen.get_width()

        # 设置标题
        pygame.display.set_caption("外星人入侵！")

        # 设置颜色
        self.bg_color = self.settings.bg_color

        # 创建一个用于统计信息的实例
        #    并创建记分牌
        self.stats = GmStats(self)
        self.sb = Scoreboard(self)

        # 创建飞船
        self.ship = Ship(self)

        # 创建子弹
        self.bullets = pygame.sprite.Group()

        # 产生外星部队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 游戏按钮
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘鼠标事件
            self._check_events()

            if self.stats.game_active:
                # 更新飞船
                self._update_ship()
                # 更新子弹组
                self._update_bullets()
                # 更新外星人
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """在玩家单击play时开始游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._start_game()

    def _start_game(self):
        """游戏开始或重新开始"""
        # 重置游戏统计信息
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        # 清空余下的外星人子弹
        self.aliens.empty()
        self.bullets.empty()
        # 创建外星人并居中飞船
        self._create_fleet()
        self.ship.center_ship()
        # 隐藏游戏光标
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """让最新绘制的屏幕可见"""
        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)
        # 飞船图像行为
        self.ship.blit_me()
        # 子弹图像行为
        for bullet in self.bullets:
            bullet.draw_bullet()
        # 外星人图像行为
        self.aliens.draw(self.screen)
        # 记分牌
        self.sb.show_score()

        # 如果游戏处于非活跃状态，则绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

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
        # 检查碰撞
        self._check_bullet_alien_collision()

    def _update_aliens(self):
        """外星部队的内容做更新"""
        # 检查是否有外星人碰壁
        self._check_fleet_edges()
        # 每个人位置移动
        self.aliens.update()
        # 检查飞船和外星人是否碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否碰到了低端
        self._check_aliens_bottom()

    def _fire_bullet(self):
        """向子弹组中加子弹"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collision(self):
        """响应子弹和外星人碰撞"""
        # 如果是，就删除子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        # 外星人没了需要新建（子弹删除）
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_fleet(self):
        # 获取创建过程中必要的数值
        alien_test = Alien(self)
        alien_width, alien_height = alien_test.rect.size
        ship_height = self.ship.rect.height
        # 计算可以容纳多少外星人
        allowed_width = self.settings.screen_width - (2 * alien_width)
        allowed_height = self.settings.screen_height - ship_height
        max_alien_num = allowed_width // (2 * alien_width)
        max_alien_rows = allowed_height // (2 * alien_height)
        # 在循环中创建外星人
        for row_num in range(0, max_alien_rows):
            for alien_num in range(0, max_alien_num):
                self._create_alien(row_num, alien_num)

    def _create_alien(self, row_num: int, alien_num: int):
        # 获取创建过程中必要的数值
        alien_test = Alien(self)
        alien_width, alien_height = alien_test.rect.size
        # 根据数量创建外星人
        new_alien = Alien(self)
        new_alien.x = alien_width + (alien_num * alien_width * 2)
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = (alien_height/2) + (row_num * alien_height * 1.5)
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """有外星人到边缘时，采取措施"""
        for e_alien in self.aliens.sprites():
            if e_alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """是否有外星人到达低端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞一样处理
                self._ship_hit()

    def _ship_hit(self):
        """响应飞船和外星人碰撞，外星人到底（即飞船毁掉）"""
        if self.stats.ships_left > 0:
            # 剩余飞船量-1
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 清除子弹和外星人
            self.aliens.empty()
            self.bullets.empty()
            # 飞船居中，创建新外星人
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.7)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _change_fleet_direction(self):
        """整群外星人下移，改变方向"""
        for e_alien in self.aliens.sprites():
            e_alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= (-1)


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
