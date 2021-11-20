import pygame
from pygame.sprite import GroupSingle

pygame.display.set_caption("Shark Game")
window_surface = pygame.display.set_mode((1200, 800))


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Import and setup sprite sheet
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png").convert_alpha(), (200, 100))
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


class Background:
    def __init__(self):
        self.image_01 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1920, 1440))
        self.image_02 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1920, 1440))  # Temp sprite
        self.rect_01 = self.image_01.get_rect(bottomleft=(0, 800))
        self.rect_02 = self.image_02.get_rect(bottomright=(0, 800))
        self.current_rect = self.rect_01

    def scroll(self):
        # TODO: Change velocity base on how big player grow
        scrolling_speed = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect_01.x += scrolling_speed
            self.rect_02.x += scrolling_speed
        if pressed_key[pygame.K_RIGHT]:
            self.rect_01.x -= scrolling_speed
            self.rect_02.x -= scrolling_speed
        if pressed_key[pygame.K_UP] and self.rect_01.top < 0:
            self.rect_01.y += scrolling_speed
            self.rect_02.y += scrolling_speed
        if pressed_key[pygame.K_DOWN] and self.rect_01.bottom > 800:
            self.rect_01.y -= scrolling_speed
            self.rect_02.y -= scrolling_speed

    def switch(self):
        # ? It works but I don't know why
        if self.current_rect.right < 600 or self.current_rect.left > 600:
            if self.current_rect == self.rect_01:
                self.current_rect.right = self.rect_02.right
                self.current_rect.left = self.rect_02.left
            if self.current_rect == self.rect_02:
                self.current_rect.right = self.rect_01.right
                self.current_rect.left = self.rect_01.left
        if self.current_rect.right < 1300:
            if self.current_rect == self.rect_01:
                self.rect_02.left = self.rect_01.right
            if self.current_rect == self.rect_02:
                self.rect_01.left = self.rect_02.right
        if self.current_rect.left > -100:
            if self.current_rect == self.rect_01:
                self.rect_02.right = self.rect_01.left
            if self.current_rect == self.rect_02:
                self.rect_01.right = self.rect_02.left


def render(shark_group: GroupSingle, background: Background):
    background.scroll()
    background.switch()
    window_surface.blit(background.image_01, background.rect_01)
    window_surface.blit(background.image_02, background.rect_02)

    shark_group.draw(window_surface)

    pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    backround = Background()

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        shark_group.update()
        render(shark_group, backround)


if __name__ == "__main__":
    main()
