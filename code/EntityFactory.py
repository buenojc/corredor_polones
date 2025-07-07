from code.Obstacle import Obstacle
from code.Player import Player
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'LevelBg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'LevelBg{i}', (0, 0)))
                    list_bg.append(Background(f'LevelBg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (30, (WIN_HEIGHT - 65)))
            case 'Obstacle0':
                return Obstacle('Obstacle0', ((WIN_WIDTH + 10), (WIN_HEIGHT - 30)))
            case 'Obstacle1':
                return Obstacle('Obstacle1', ((WIN_WIDTH + 10), (WIN_HEIGHT - 30)))
            case 'Obstacle2':
                return Obstacle('Obstacle2', ((WIN_WIDTH + 10), (WIN_HEIGHT - 30)))
        return None
