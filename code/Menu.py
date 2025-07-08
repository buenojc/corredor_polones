import pygame.display
from pygame import Surface, K_DOWN

from code.Const import MENU_OPTIONS, WIN_WIDTH, C_WHITE, C_RED, C_BRIGHT_RED, C_LIGHT_BLUE
from code.utils import screen_text


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('../assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        # Load and play music
        pygame.mixer.music.load('../assets/MenuSd.mp3')
        pygame.mixer_music.play(-1)

        option_selected = 0
        while True:
            self.window.blit(self.surf, self.rect)
            screen_text(self.window, 60, 'RUNNING', C_WHITE, ((WIN_WIDTH / 2), 40))
            screen_text(self.window, 60, 'KNIGHT', C_RED, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTIONS)):
                if i == option_selected:
                    screen_text(self.window, 30, MENU_OPTIONS[i], C_BRIGHT_RED, ((WIN_WIDTH / 2), (200 + 35 * i)))
                else:
                    screen_text(self.window, 30, MENU_OPTIONS[i], C_LIGHT_BLUE, ((WIN_WIDTH / 2), (200 + 35 * i)))



            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if option_selected == len(MENU_OPTIONS) - 1:
                            option_selected = 0
                        else:
                            option_selected += 1

                    if event.key == pygame.K_UP:
                        if option_selected == 0:
                            option_selected = len(MENU_OPTIONS) - 1
                        else:
                            option_selected -= 1

                    if event.key == pygame.K_RETURN:
                        return option_selected
