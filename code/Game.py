import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        print('Starting Game')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            selected_menu = menu.run()

            if selected_menu == 2:
                pygame.quit()
                quit()

