import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import time


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 设置分辨率
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏主循环"""
        # i=1
        while True:
            # time.sleep(1)
            # i+=1
            # print(i)
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """监视鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        self.bullets.update() #更新子弹的位置
        for bullet in self.bullets.copy():  # 删除消失的子弹
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中。"""
        new_bullet = Bullet(self)
        if len(self.bullets)<self.settings.bullets_allowed:
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 每次循环重新画背景屏幕
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """让最近绘制的图像可见"""
        pygame.display.flip()


if __name__ == "__main__":
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
