class GmStats:
    """跟踪游戏的统计类"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动处于活动状态
        self.game_active = False

        # 飞船还剩几艘
        self.ships_left = self.settings.ship_limit
        # 积分
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏内的统计信息"""
        # 重置飞船数
        self.ships_left = self.settings.ship_limit
        # 重置分数
        self.score = 0
