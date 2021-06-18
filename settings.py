class Settings:
    """存储游戏《外星人入侵》中所有的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5  # 飞船设置

        self.bullet_speed =1.0
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 10
