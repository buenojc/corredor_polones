import random

import pygame.event
from pygame import Surface

from code.Const import EVENT_OBSTACLE, SPAWN_TIME, C_BRIGHT_RED, C_RED, C_WHITE, C_GREEN, C_LIGHT_BLUE, C_ORANGE, \
    C_YELLOW, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.utils import screen_text


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
        # Load and play music
        pygame.mixer.music.load('../assets/LevelSd.mp3')
        pygame.mixer_music.play(-1)
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

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return

                    if event.type == EVENT_OBSTACLE:
                        choice = random.choice(('Obstacle0', 'Obstacle1', 'Obstacle2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return self.player.score

            screen_text(self.window, 30, f'Health: {self.player.health}', C_ORANGE, (60, 30))
            screen_text(self.window, 30, f'Points: {self.player.score}', C_YELLOW, ((WIN_WIDTH - 80), 30))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(self.entity_list, self.player)
            pygame.display.flip()