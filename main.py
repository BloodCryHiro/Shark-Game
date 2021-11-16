import pygame

pygame.display.set_caption("Shark Game")
window_surface = pygame.display.set_mode((1200, 800))


def render():
    background = pygame.image.load()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    main()
