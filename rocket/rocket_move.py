import pygame
import sys
from rocket import Rocket


class MoveRocket(object):
    """移动火箭用的游戏类"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1100, 750))
        pygame.display.set_caption("火箭游戏！")

        self.rocket = Rocket(self)

    def run_geme(self):
        while True:
            # ×号标记
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # 点击响应
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rocket.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = True
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.rocket.moving_down = True
                # 松开响应
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.rocket.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = False
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.rocket.moving_down = False


            # 刷新屏幕
            self.screen.fill((200, 200, 200))
            self.rocket.blit_me()
            pygame.display.flip()
            pygame.time.delay(2)


if __name__ == '__main__':
    move_rocket = MoveRocket()
    move_rocket.run_geme()

