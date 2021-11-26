import pygame
from background import Background


class SpriteManager:
    def __init__(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.scrolling_speed = 5  # TODO: Change velocity base on how big player grow

    # TODO: Parallax Scrolling
    # ! Weird bug when reach the border
    # ! Fish keep moving when press up and down at the same time
    def background_scroll(self, background: Background):
        pressed_key = pygame.key.get_pressed()
        for sprite in self.all_sprites:
            if pressed_key[pygame.K_LEFT]:
                sprite.rect.x += self.scrolling_speed
            if pressed_key[pygame.K_RIGHT]:
                sprite.rect.x -= self.scrolling_speed
            if pressed_key[pygame.K_UP] and background.rect.top < 0:
                sprite.rect.y += self.scrolling_speed
            if pressed_key[pygame.K_DOWN] and background.rect.bottom > 800:
                sprite.rect.y -= self.scrolling_speed
