import pygame
from pygame import Surface

from code.Const import C_WHITE, WIN_WIDTH
from code.utils import screen_text


class Instructions:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('../assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)
            screen_text(self.window, 60, 'Welcome to Running Knight!', C_WHITE, ((WIN_WIDTH / 2), 40))
            screen_text(self.window, 22, 'Your objective is to avoid the obstacle', C_WHITE, ((WIN_WIDTH / 2), 100))
            screen_text(self.window, 22, 'by jumping when press SPACE.', C_WHITE, ((WIN_WIDTH / 2), 130))
            screen_text(self.window, 22, 'When you die you will be able to save your score.', C_WHITE,
                        ((WIN_WIDTH / 2), 160))
            screen_text(self.window, 25, 'Enjoy!', C_WHITE, ((WIN_WIDTH / 2), 200))
            screen_text(self.window, 35, 'PRESS ENTER TO CONTINUE', C_WHITE, ((WIN_WIDTH / 2), 300))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True

                    if event.key == pygame.K_ESCAPE:
                        return False
