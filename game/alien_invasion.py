import pygame
from settings import Settings
from ship import Ship
import game_funcations as gf

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(settings,screen)
    bullets = pygame.sprite.Group()
    while True:
        #监测鼠标键盘事件
        gf.check_events(ship,settings,screen,bullets)
        ship.update()
        bullets.update()
        #更新屏幕
        gf.update_screen(settings, screen, ship, bullets)

# if __name__ == '__main__':
run_game()