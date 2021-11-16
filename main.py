import pygame

pygame.display.set_caption("Shark Game")
window_surface = pygame.display.set_mode((1200, 800))


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png").convert_alpha(), (200, 100))
        self.rect = self.image.get_rect(bottomleft=(600, 600))


def render(shark_group):
    background = pygame.transform.scale(
        pygame.image.load("Assets/Arts/background.png"), (1280, 960))

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

        render(shark_group)


if __name__ == "__main__":
    main()
