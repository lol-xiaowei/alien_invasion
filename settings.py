class Settings:
    """存放系统设置的类"""
    def __init__(self):
        # 窗口设置
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.8

        # 子弹设置
        self.bullet_color = (255, 153, 18)
        self.bullet_width = 3
        self.bullet_height = 15

        self.bullet_speed = 0.8
        self.bullet_allowed = 3
