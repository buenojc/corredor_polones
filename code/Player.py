import pygame.key
from pygame import K_SPACE

from code.Const import WIN_HEIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.sprites = []
        for i in range(6):
            self.sprites.append(pygame.image.load(f'../assets/Player{i}.png').convert_alpha())
        self.surf = self.sprites[1]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_strength = -15
        self.is_jumping = False
        self.ground_y = WIN_HEIGHT - 65
        self.position = position
        self.sprite = 1

        self.current_frame = 0
        self.frame_delay = 8
        self.frame_counter = 0

    def _update(self):
        # Use to make the jump smooth
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.is_jumping = False

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            if not self.is_jumping:
                self.velocity_y = self.jump_strength
                self.is_jumping = True
        # Call the method to update player position through the jump
        self._update()
        # Animate Running and Jumping
        self.animate()


    def animate(self):
        if not self.is_jumping:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.current_frame = (self.current_frame + 1) % len(self.sprites)
                self.surf = self.sprites[self.current_frame]
                self.frame_counter = 0
        else:
            # When jumping
            self.surf = self.sprites[0]

