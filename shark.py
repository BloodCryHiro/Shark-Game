import pygame
from fish import Fish


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Import and setup sprite sheet
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png").convert_alpha(), (100, 50))
        self.size = 1
        self.rect = self.image.get_rect(center=(600, 400))
        self.isRight = True

    def get_direction(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            if self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isRight = False
        if pressed_key[pygame.K_RIGHT]:
            if not self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
                self.isRight = True

    def collision_fish(self, fish: Fish):
        if self.size >= fish.size:
            # Become bigger and faster
            self.size += 0.5
            self.image = pygame.transform.scale(
                self.image, (self.size * 100, self.size * 50))
            # Gain more health
            # Get score
            # Get poisoned
            fish.collision_shark()
        else:
            # Get hurt
            # Become invisible for a while
            pass

    def update(self):
        self.get_direction()
