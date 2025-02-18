import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # for later use
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(self.x, self.y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # for overriding by subclass
        pass

    def update(self, dt):
        # for overriding by subclass
        pass
