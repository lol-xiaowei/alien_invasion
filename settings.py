class Settings:
    """存放系统设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 窗口设置
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 1.2
        self.ship_limit = 2
        # 子弹设置
        self.bullet_color = (255, 153, 18)
        self.bullet_width = 12
        self.bullet_height = 30
        self.bullet_speed = 2
        self.bullet_allowed = 50
        # 外星人设置
        self.alien_speed = 0.5
        self.fleet_drop_speed = 18
        self.fleet_direction = 1
        self.alien_points = 50

        # 加快游戏速度
        self.speedup_scale = 1.3
        self.score_scale = 2

        # 设置初始化
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        """难度升级"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # 得分升级
        self.alien_points = int(self.alien_points * self.score_scale)
