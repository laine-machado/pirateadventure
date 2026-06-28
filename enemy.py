import pygame
import random

from settings import *


class Enemy:

    def __init__(self, world_width, player, speed_range):

        # ==========================
        # ESCOLHE IMAGEM
        # ==========================

        image_name = random.choice([
            "enemy1.png",
            "enemy2.png"
        ])

        self.image = pygame.image.load(
            f"assets/images/{image_name}"
        ).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image,
            (ENEMY_WIDTH, ENEMY_HEIGHT)
        )

        # ==========================
        # POSIÇÃO
        # ==========================

        self.rect = self.image.get_rect()

        self.rect.y = GROUND_Y - ENEMY_HEIGHT

        # ==========================
        # VELOCIDADE
        # ==========================

        speed = random.randint(
            speed_range[0],
            speed_range[1]
        )

        # ==========================
        # NASCE NA FRENTE DO JOGADOR
        # ==========================

        distance = random.randint(900, 1300)

        if player.direction == "right":

            self.rect.x = min(
                player.rect.x + distance,
                world_width - ENEMY_WIDTH
            )

            self.speed = -speed

        else:

            self.rect.x = max(
                player.rect.x - distance,
                0
            )

            self.speed = speed

        # ==========================
        # HITBOX
        # ==========================

        self.hitbox = pygame.Rect(0, 0, 140, 160)

        self.update_hitbox()

    # ==================================

    def update_hitbox(self):

        self.hitbox.x = self.rect.x + 20
        self.hitbox.y = self.rect.y + 15

    # ==================================

    def update(self):

        self.rect.x += self.speed

        self.update_hitbox()

    # ==================================

    def draw(self, screen, camera_x):

        screen.blit(

            self.image,

            (

                self.rect.x - camera_x,

                self.rect.y

            )

        )

        # -------------------------
        # DEBUG HITBOX
        # Descomente para visualizar
        #
        # pygame.draw.rect(
        #     screen,
        #     (255,0,0),
        #     (
        #         self.hitbox.x-camera_x,
        #         self.hitbox.y,
        #         self.hitbox.width,
        #         self.hitbox.height
        #     ),
        #     2
        # )

    # ==================================

    def collides(self, player):

        return self.hitbox.colliderect(player.rect)

    # ==================================

    def is_off_screen(self, camera_x):

        if self.rect.right < camera_x - 300:
            return True

        if self.rect.left > camera_x + WIDTH + 300:
            return True

        return False