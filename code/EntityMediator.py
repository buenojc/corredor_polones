from code.Entity import Entity
from code.Obstacle import Obstacle
from code.Player import Player


class EntityMediator:
    @staticmethod
    def _verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_interaction = False
        player = None
        obstacle = None
        if isinstance(ent1, Player) and isinstance(ent2, Obstacle):
            valid_interaction = True
            player = ent1
            obstacle = ent2

        if isinstance(ent2, Player) and isinstance(ent1, Obstacle):
            valid_interaction = True
            player = ent2
            obstacle = ent1
        if valid_interaction:
            # Using method to check collision from pygame
            if player.rect.colliderect(obstacle.rect):
                if not obstacle.interacting:
                    player.health -= obstacle.damage
                    obstacle.collided = True
                    # Using this flag to make sure player will only be hit once per obstacle
                    obstacle.interacting = True
            else:
                obstacle.interacting = False

    @staticmethod
    def _verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacle):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_1 = entity_list[i]
            EntityMediator._verify_collision_window(entity_1)
            for j in range(i + 1, len(entity_list)):
                entity_2 = entity_list[j]
                EntityMediator._verify_collision_entity(entity_1, entity_2)



    @staticmethod
    def verify_health(entity_list: list[Entity], player: Player):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Obstacle):
                    # Every obstacle that has 0 health AND has not collided with player gives point, otherwise no point
                    if not ent.collided:
                        EntityMediator._give_score(ent, player)
                entity_list.remove(ent)

    @staticmethod
    def _give_score(obstacle: Obstacle, player: Player):
        player.score += obstacle.points
