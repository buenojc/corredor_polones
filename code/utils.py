import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import GAME_FONT


def screen_text(window: Surface, text_size: int, text: str, text_color: tuple, text_center_pos: tuple ):
    text_font: Font = pygame.font.SysFont(name=GAME_FONT, size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color)
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    window.blit(source=text_surf, dest=text_rect)