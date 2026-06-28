import pygame
from settings import *


class Player:

    def __init__(self):

        # ===============================
        # IMAGEM
        # ===============================

        self.image = pygame.image.load(
            "assets/images/player.png"
        ).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        # ===============================
        # POSIÇÃO
        # ===============================

        self.rect = self.image.get_rect()

        self.rect.x = 150
        self.rect.y = GROUND_Y - PLAYER_HEIGHT

        # ===============================
        # MOVIMENTO
        # ===============================

        self.speed = PLAYER_SPEED

        self.direction = "right"

        # Movimento vertical
        self.velocity_y = 0

        self.on_ground = True

    # ==========================================

    def move(self):

        keys = pygame.key.get_pressed()

        # ------------------------------
        # ESQUERDA
        # ------------------------------

        if keys[pygame.K_LEFT]:

            self.rect.x -= self.speed

            self.direction = "left"

        # ------------------------------
        # DIREITA
        # ------------------------------

        if keys[pygame.K_RIGHT]:

            self.rect.x += self.speed

            self.direction = "right"

        # ------------------------------
        # PULO
        # ------------------------------

        if keys[pygame.K_SPACE] and self.on_ground:

            self.velocity_y = PLAYER_JUMP

            self.on_ground = False

    # ==========================================

    def gravity(self):

        self.velocity_y += GRAVITY

        self.rect.y += self.velocity_y

        if self.rect.bottom >= GROUND_Y:

            self.rect.bottom = GROUND_Y

            self.velocity_y = 0

            self.on_ground = True

    # ==========================================

    def limit_world(self, world_width):

        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > world_width:

            self.rect.right = world_width

    # ==========================================

    def update(self, world_width):

        self.move()

        self.gravity()

        self.limit_world(world_width)

    # ==========================================

    def draw(self, screen, camera_x):

        screen.blit(

            self.image,

            (

                self.rect.x - camera_x,

                self.rect.y

            )

        )