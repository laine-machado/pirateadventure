import pygame
import random

from settings import *

from player import Player
from enemy import Enemy
from coin import Coin
from camera import Camera
from hud import HUD
from level import Level


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.clock = pygame.time.Clock()

        # ==========================
        # MUNDO
        # ==========================

        self.world_width = WORLD_WIDTH

        # ==========================
        # FASE
        # ==========================

        self.level = Level()

        # ==========================
        # HUD
        # ==========================

        self.hud = HUD()

        # ==========================
        # PLAYER
        # ==========================

        self.player = Player()

        # ==========================
        # CAMERA
        # ==========================

        self.camera = Camera(self.world_width)

        # ==========================
        # LISTAS
        # ==========================

        self.coins = []

        self.enemies = []

        # ==========================
        # CONTADORES
        # ==========================

        self.collected = 0

        self.score = 0

        # ==========================
        # ESTADOS
        # ==========================

        self.game_over = False

        self.game_finished = False

        self.paused = False

        # ==========================
        # SPAWN
        # ==========================

        self.spawn_timer = 0

        self.spawn_delay = 0

        # ==========================
        # CENÁRIO
        # ==========================

        self.background = None

        self.background_width = WIDTH

        self.load_background()

        self.create_level()

    # =======================================================
    # CARREGA O CENÁRIO
    # =======================================================

    def load_background(self):

        self.background = pygame.image.load(
            self.level.background
        ).convert()

        largura = self.background.get_width()
        altura = self.background.get_height()

        escala = HEIGHT / altura

        largura = int(largura * escala)

        self.background = pygame.transform.smoothscale(

            self.background,

            (

                largura,

                HEIGHT

            )

        )

        self.background_width = largura

    # =======================================================
    # CRIA A FASE
    # =======================================================

    def create_level(self):

        print("Criando fase...")

        # -------------------------
        # LIMPA LISTAS
        # -------------------------

        self.coins.clear()

        self.enemies.clear()

        # -------------------------
        # MOEDAS
        # -------------------------

        used_positions = []

        for _ in range(self.level.goal):

            self.coins.append(

                Coin(

                    self.world_width,

                    used_positions

                )

            )

        # -------------------------
        # SPAWN
        # -------------------------

        self.spawn_timer = 0

        self.spawn_delay = random.randint(

            self.level.spawn_time[0],

            self.level.spawn_time[1]

        )

        # -------------------------
        # CONTADOR
        # -------------------------

        self.collected = 0

        print("Fase criada!")

    # =======================================================
    # REINICIAR
    # =======================================================

    def restart(self):

        self.player = Player()

        self.camera = Camera(self.world_width)

        self.score = 0

        self.game_over = False

        self.game_finished = False

        self.create_level()

    # =======================================================
    # UPDATE
    # =======================================================

    def update(self):

        if self.game_over:
            return

        if self.game_finished:
            return

        if self.paused:
            return

        # ------------------------------------
        # PLAYER
        # ------------------------------------

        self.player.update(self.world_width)

        # ------------------------------------
        # CAMERA
        # ------------------------------------

        self.camera.update(self.player)

        camera_x = self.camera.get_offset()

        # ------------------------------------
        # MOEDAS
        # ------------------------------------

        for coin in self.coins:

            if coin.update(self.player):

                self.collected += 1

                self.score += 100

        # ------------------------------------
        # PASSOU DE FASE
        # ------------------------------------

        if self.collected >= self.level.goal:

            self.score += 500

            if self.level.next_level():

                self.load_background()

                self.player = Player()

                self.camera = Camera(self.world_width)

                self.create_level()

            else:

                self.game_finished = True

            return

        # ------------------------------------
        # SPAWN DOS INIMIGOS
        # ------------------------------------

        self.spawn_timer += 1

        if (

            self.spawn_timer >= self.spawn_delay

            and

            len(self.enemies) < self.level.max_enemies

        ):

            self.enemies.append(

                Enemy(

                    self.world_width,

                    self.player,

                    self.level.enemy_speed

                )

            )

            self.spawn_timer = 0

            self.spawn_delay = random.randint(

                self.level.spawn_time[0],

                self.level.spawn_time[1]

            )

        # ------------------------------------
        # INIMIGOS
        # ------------------------------------

        for enemy in self.enemies:

            enemy.update()

            if enemy.collides(self.player):

                self.game_over = True

        # ------------------------------------
        # REMOVE INIMIGOS
        # ------------------------------------

        self.enemies = [

            enemy

            for enemy in self.enemies

            if not enemy.is_off_screen(camera_x)

        ]

    # =======================================================
    # DRAW
    # =======================================================

    def draw(self):

        camera_x = self.camera.get_offset()

        # ------------------------------------
        # CENÁRIO
        # ------------------------------------

        x = -camera_x % self.background_width - self.background_width

        while x < WIDTH:

            self.screen.blit(

                self.background,

                (x, 0)

            )

            x += self.background_width

        # ------------------------------------
        # MOEDAS
        # ------------------------------------

        for coin in self.coins:

            coin.draw(

                self.screen,

                camera_x

            )

        # ------------------------------------
        # INIMIGOS
        # ------------------------------------

        for enemy in self.enemies:

            enemy.draw(

                self.screen,

                camera_x

            )

        # ------------------------------------
        # PLAYER
        # ------------------------------------

        self.player.draw(

            self.screen,

            camera_x

        )

        # ------------------------------------
        # HUD
        # ------------------------------------

        self.hud.draw(

            self.screen,

            self.collected,

            self.level.goal,

            self.score,

            self.level.current

        )

        # ------------------------------------
        # GAME OVER
        # ------------------------------------

        if self.game_over:

            self.hud.draw_game_over(

                self.screen

            )

        # ------------------------------------
        # VITÓRIA
        # ------------------------------------

        if self.game_finished:

            self.hud.draw_victory(

                self.screen

            )

        # ------------------------------------
        # PAUSA
        # ------------------------------------

        if self.paused:

            self.hud.draw_pause(

                self.screen

            )

        pygame.display.flip()

    # =======================================================
    # LOOP PRINCIPAL
    # =======================================================

    def run(self):

        while True:

            self.clock.tick(FPS)

            # ----------------------------------
            # EVENTOS
            # ----------------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    return "quit"

                if event.type == pygame.KEYDOWN:

                    # --------------------------
                    # MENU
                    # --------------------------

                    if event.key == pygame.K_ESCAPE:

                        return "menu"

                    # --------------------------
                    # PAUSA
                    # --------------------------

                    elif event.key == pygame.K_p:

                        self.paused = not self.paused

                    # --------------------------
                    # REINICIAR
                    # --------------------------

                    elif event.key == pygame.K_RETURN:

                        if self.game_over:

                            self.level.reset()

                            self.load_background()

                            self.restart()

                        elif self.game_finished:

                            self.level.reset()

                            return "menu"

            # ----------------------------------
            # UPDATE
            # ----------------------------------

            self.update()

            # ----------------------------------
            # DRAW
            # ----------------------------------

            self.draw()