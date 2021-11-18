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


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1280, 960))
        self.rect = self.image.get_rect(bottomleft=(0, 800))

    def scrolling(self):
        # TODO: Change velocity base on how big player grow
        scrolling_speed = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect.x += scrolling_speed
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x -= scrolling_speed
        if pressed_key[pygame.K_UP]:
            self.rect.y += scrolling_speed
        if pressed_key[pygame.K_DOWN]:
            self.rect.y -= scrolling_speed

    def update(self):
        self.scrolling()


def render(shark_group: GroupSingle, background_group: GroupSingle):
    background_group.draw(window_surface)
    shark_group.draw(window_surface)

    pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    backround = Background()
    backround_group = pygame.sprite.GroupSingle()
    backround_group.add(backround)

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        backround_group.update()
        shark_group.update()
        render(shark_group, backround_group)


if __name__ == "__main__":
    main()
