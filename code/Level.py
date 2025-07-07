import random
from random import choice

import pygame.event
from pygame import Surface

from code.Const import EVENT_OBSTACLE, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, name:str, window: Surface):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)
        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == EVENT_OBSTACLE:
                        choice = random.choice(('Obstacle0', 'Obstacle1', 'Obstacle2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))


            pygame.display.flip()