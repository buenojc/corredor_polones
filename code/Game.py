import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Instructions import Instructions
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        print('Starting Game')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            selected_menu = menu.run()

            if selected_menu == 0:
                instructions = Instructions(window=self.window)
                return_instructions = instructions.run()
                if return_instructions:
                    level = Level(window=self.window, name='Level')
                    return_level_score = level.run()
                    if return_level_score:
                        score.save(return_level_score)

            elif selected_menu == 1:
                score.show()

            elif selected_menu == 2:
                pygame.quit()
                quit()
