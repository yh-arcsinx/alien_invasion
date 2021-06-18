import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")  # 加载飞船并获取外接矩形
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom  # 对于每艘新飞船，都将其放在屏幕的底部中央
        self.x = float(self.rect.x)  # 在飞船的属性x中存储小数值
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 在指定位置绘制飞船
