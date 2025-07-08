from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, K_BACKSPACE, K_ESCAPE

from code.Const import C_YELLOW, SCORE_POS, C_WHITE, C_RED
from code.DBProxy import DBProxy

from code.utils import screen_text


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('../assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, score):
        # pygame.mixer_music.load(f'./asset/Score.mp3')
        # pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            screen_text(self.window,48, 'WELL DONE!!', C_YELLOW, SCORE_POS['Title'])

            text = 'Enter Player 1 name (4 characters):'
            screen_text(self.window,20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return

                    if event.key == K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 4:
                            name += event.unicode

            screen_text(self.window,20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        # Load and play music
        pygame.mixer_music.load(f'../assets/ScoreSd.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        self.window.blit(source=self.surf, dest=self.rect)
        screen_text(self.window,48, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Title'])
        screen_text(self.window,20, 'NAME   SCORE     DATE          ', C_WHITE, SCORE_POS['Label'])

        for player_score in list_score:
            id_, name, score, date = player_score
            screen_text(self.window,20, f'{name}     {score :.0f}       {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return



def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d:%m:%y")
    return f"{current_time} - {current_date}"
