import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_01 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background.png").convert_alpha(), (1920, 1440))
        self.image_02 = pygame.transform.scale(
            pygame.image.load("Assets/Arts/background_test.png").convert_alpha(), (1920, 1440))  # Temp sprite

        self.image = pygame.Surface((1920 * 2, 1440))
        self.rect = self.image.get_rect(midbottom=(0, 800))
        self.image.blit(self.image_01, (1920, 0))
        self.image.blit(self.image_02, (0, 0))
        self.image_right = 1

        self.background_switch_right = pygame.USEREVENT + 1
        self.background_switch_left = pygame.USEREVENT + 2

    def switch(self):
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
            pygame.event.post(pygame.event.Event(self.background_switch_left))
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
            pygame.event.post(pygame.event.Event(self.background_switch_right))

    def update(self):
        self.switch()
