import pygame
from pygame.sprite import Group, GroupSingle
from config import *
from background import Background
from shark import Shark
from fish import Fish
from sprite_manager import SpriteManager

pygame.init()
pygame.display.set_caption("Shark Game")
window_surface = pygame.display.set_mode((1200, 800))


def collision(shark_group: GroupSingle, fish_group: Group):
    shark_fish_collision_list = pygame.sprite.spritecollide(
        shark_group.sprite, fish_group, False)

    if shark_fish_collision_list:
        pygame.event.post(pygame.event.Event(SHARK_FISH_COLLITSION))
        return shark_fish_collision_list


def render(shark_group: GroupSingle, fish_group: Group, background_group: GroupSingle, background: Background, sprite_manager: SpriteManager):
    sprite_manager.background_scroll(background)

    background_group.update()
    background_group.draw(window_surface)

    fish_group.draw(window_surface)

    shark_group.update()
    shark_group.draw(window_surface)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    sprite_manager = SpriteManager()

    background = Background()
    background_group = pygame.sprite.GroupSingle()
    background_group.add(background)
    sprite_manager.all_sprites.add(background)

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    fish_group = pygame.sprite.Group()
    for i in range(0, 5):
        fish = Fish()
        fish_group.add(fish)
        sprite_manager.all_sprites.add(fish)

    while True:
        clock.tick(60)

        shark_fish_collision_list = collision(shark_group, fish_group)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == BACKGROUND_SWITCH_RIGHT:
                fish: Fish
                for fish in fish_group.sprites():
                    fish.switch("right")
            if event.type == BACKGROUND_SWITCH_LEFT:
                fish: Fish
                for fish in fish_group.sprites():
                    fish.switch("left")
            if event.type == SHARK_FISH_COLLITSION:
                shark.collision_fish(shark_fish_collision_list[0])

        render(shark_group, fish_group, background_group,
               background, sprite_manager)


if __name__ == "__main__":
    main()
