import sys
import pygame
from bullet import Bullet


def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)
    #重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()

def check_keydown_events(event, ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        # 右移飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 左移飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 右移飞船停止
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 左移飞船停止
        ship.moving_left = False