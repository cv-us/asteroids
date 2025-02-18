import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = [drawable, updatable]
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        #limit frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
