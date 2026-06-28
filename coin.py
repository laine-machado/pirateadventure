import pygame
import random

from settings import *


class Coin:

    def __init__(self, world_width, used_positions=None):

        if used_positions is None:
            used_positions = []

        # ==========================
        # IMAGEM
        # ==========================

        self.image = pygame.image.load(
            "assets/images/coin.png"
        ).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image,
            (COIN_SIZE, COIN_SIZE)
        )

        self.rect = self.image.get_rect()

        # ==========================
        # POSIÇÃO X
        # ==========================

        for _ in range(1000):

            x = random.randint(300, world_width - 300)

            valido = True

            for pos in used_positions:

                if abs(x - pos) < 180:
                    valido = False
                    break

            if valido:
                self.rect.x = x
                used_positions.append(x)
                break
        else:

            self.rect.x = random.randint(300, world_width - 300)

        # ==========================
        # POSIÇÃO Y
        # ==========================

        altura = random.choice([
            0,
            0,
            0,
            60,
            100
        ])

        self.rect.y = GROUND_Y - COIN_SIZE - altura

        self.collected = False

    # ==================================

    def update(self, player):

        if self.collected:
            return False

        if self.rect.colliderect(player.rect):

            self.collected = True

            return True

        return False

    # ==================================

    def draw(self, screen, camera_x):

        if not self.collected:

            screen.blit(

                self.image,

                (

                    self.rect.x - camera_x,

                    self.rect.y

                )

            )