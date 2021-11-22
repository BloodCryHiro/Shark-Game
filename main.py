import random
import pygame
from pygame.sprite import Group, GroupSingle

pygame.display.set_caption("Shark Game")
window_surface = pygame.display.set_mode((1200, 800))


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Import and setup sprite sheet
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png").convert_alpha(), (100, 50))
        self.rect = self.image.get_rect(center=(600, 400))
        self.isRight = True

    def get_direction(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            if self.isRight == True:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isRight = False
        if pressed_key[pygame.K_RIGHT]:
            if self.isRight == False:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isRight = True

    def update(self):
        self.get_direction()


class Fish(pygame.sprite.Sprite):
    # ? Using color, size and position arg or not?
    def __init__(self):
        super().__init__()
        # Temp, Depend on color argument
        image_source = pygame.image.load(
            "Assets/Arts/fish.png").convert_alpha()
        size = random.randint(1, 3)
        self.image = pygame.transform.scale(
            image_source, (size * 100, size * 50))
        self.rect = self.image.get_rect(
            center=(random.randint(100, 1920 * 2 - 100), random.randint(100, 1440 - 100)))
        # ? How to make fish instances switch with background
        if self.rect.x > 1920:
            self.position_in_map = "Right"
        else:
            self.position_in_map = "Left"


class Background:
    def __init__(self):
        self.image_01 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1920, 1440))
        self.image_02 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background_test.png").convert_alpha(), (1920, 1440))  # Temp sprite

        self.image = pygame.Surface((1920 * 2, 1440))
        self.rect = self.image.get_rect(midbottom=(0, 800))
        self.image.blit(self.image_01, (1920, 0))
        self.image.blit(self.image_02, (0, 0))
        self.image_right = 1

    # TODO: Parolox Scrolling

    def scroll(self):
        # TODO: Change velocity base on how big player grow
        scrolling_speed = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect.x += scrolling_speed
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x -= scrolling_speed
        if pressed_key[pygame.K_UP] and self.rect.top < 0:
            self.rect.y += scrolling_speed
        if pressed_key[pygame.K_DOWN] and self.rect.bottom > 800:
            self.rect.y -= scrolling_speed

    def switch(self):
        # FIXME: Doesn't work normally. Fish will stuck at the initial position on self.image
        if 0 - self.rect.left < 200:
            if self.image_right == 1:
                self.image.blit(self.image_01, (0, 0))
                self.image.blit(self.image_02, (1920, 0))
                self.image_right = 2
            elif self.image_right == 2:
                self.image.blit(self.image_01, (1920, 0))
                self.image.blit(self.image_02, (0, 0))
                self.image_right = 1
            self.rect.x -= 1920
        elif self.rect.right - 1200 < 200:
            if self.image_right == 1:
                self.image.blit(self.image_01, (0, 0))
                self.image.blit(self.image_02, (1920, 0))
                self.image_right = 2
            elif self.image_right == 2:
                self.image.blit(self.image_01, (1920, 0))
                self.image.blit(self.image_02, (0, 0))
                self.image_right = 1
            self.rect.x += 1920


def render(shark_group: GroupSingle, fish_group: Group, background: Background):
    background.scroll()
    background.switch()
    fish_group.draw(background.image)
    window_surface.blit(background.image, background.rect)

    shark_group.update()
    shark_group.draw(window_surface)

    pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    backround = Background()

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    fish_group = pygame.sprite.Group()
    for i in range(0, 5):
        fish_group.add(Fish())

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        render(shark_group, fish_group, backround)


if __name__ == "__main__":
    main()
