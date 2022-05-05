import pygame
import sys


class KeyDown:
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((1100, 750))
        pygame.display.set_caption("看看各种键盘响应")

    def run_program(self):
        while True:
            for event in pygame.event.get():
                # ×号标记
                if event.type == pygame.QUIT:
                    sys.exit()
                # 响应
                if event.type == pygame.KEYDOWN:
                    print(event.key)


if __name__ == '__main__':
    key = KeyDown()
    key.run_program()
