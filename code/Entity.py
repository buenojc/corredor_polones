from abc import abstractmethod, ABC

import pygame.image

from code.Const import ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        if self.name != 'Player':
            # Player has animations, so this avoids sprites been loaded twice
            self.surf = pygame.image.load('../assets/' + name + '.png').convert_alpha()
            self.rect = self.surf.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
