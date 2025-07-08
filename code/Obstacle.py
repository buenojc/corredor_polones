from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_POINTS
from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Health and Damage
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.points = ENTITY_POINTS[self.name]
        self.collided = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]