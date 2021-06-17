import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")  # 加载飞船并获取外接矩形
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom  # 对于每艘新飞船，都将其放在屏幕的底部中央
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 在指定位置绘制飞船
