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
        self.rect = self.image.get_rect(bottomleft=(600, 600))

    def movement(self):
        # TODO: Change velocity base on how big player grow
        shark_velocity = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= shark_velocity
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += shark_velocity
        if pressed_key[pygame.K_UP]:
            self.rect.y -= shark_velocity
        if pressed_key[pygame.K_DOWN]:
            self.rect.y += shark_velocity

    def update(self):
        self.movement()


def render(shark_group: GroupSingle):
    background = pygame.transform.scale(
        pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1280, 960))

    window_surface.blit(background, (0, 800 - 960))
    shark_group.draw(window_surface)

    pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        shark_group.update()
        render(shark_group)


if __name__ == "__main__":
    main()
