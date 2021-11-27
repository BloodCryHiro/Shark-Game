import pygame
import random


class Fish(pygame.sprite.Sprite):
    # ? Using color, size and position arg or not?
    def __init__(self):
        super().__init__()
        # Temp, Depend on color argument
        image_source = pygame.image.load(
            "Assets/Arts/fish.png").convert_alpha()
        self.size = random.random() * 3
        self.speed = self.size * 5  # * Speed is based on size
        self.image = pygame.transform.scale(
            image_source, (self.size * 100, self.size * 50))
        self.rect = self.image.get_rect(
            center=(random.randint(-1920 + 100, 1920 - 100), random.randint(100, 700)))
        if self.rect.x > 0:
            self.position_in_map = "right"
        else:
            self.position_in_map = "left"

        self.isAlive = True

    def switch(self, direction):
        if direction == "left":
            if self.position_in_map == "right":
                self.rect.x -= 1920 * 2
                self.position_in_map = "left"
            else:
                self.position_in_map = "right"
        elif direction == "right":
            if self.position_in_map == "left":
                self.rect.x += 1920 * 2
                self.position_in_map = "right"
            else:
                self.position_in_map = "left"

    def collision_shark(self):
        # move to a point player can't see
        self.rect.x = 0
        self.rect.y = 3000
        self.isAlive = False
        # can't move and switch

    # def movement(self, shark: Shark):
    #     if distance_to_shark < (500, 500):
    #         # Move casually
    #         pass
    #     else:
    #         if self.size > shark.size:
    #             # Move toward shark and try to attack
    #             pass
    #         elif self.size == shark.size:
    #             # Move casually
    #             pass
    #         else:
    #             # Move away from shark and try to escape
    #             pass
