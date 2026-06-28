import pygame
from settings import *


class Menu:

    def __init__(self, screen):

        self.screen = screen

        # ======================================
        # IMAGEM DE FUNDO
        # ======================================

        self.background = pygame.image.load(
            "assets/images/menu_background.png"
        ).convert()

        self.background = pygame.transform.smoothscale(
            self.background,
            (WIDTH, HEIGHT)
        )

        # ======================================
        # FONTES
        # ======================================

        self.title_font = pygame.font.SysFont(
            "Arial",
            72,
            True
        )

        self.option_font = pygame.font.SysFont(
            "Arial",
            42,
            True
        )

        self.footer_font = pygame.font.SysFont(
            "Arial",
            20
        )

        # ======================================
        # OPÇÕES
        # ======================================

        self.options = [

            "Novo Jogo",

            "Instruções",

            "Sair"

        ]

        self.selected = 0

    # =====================================================

    def draw(self):

        self.screen.blit(self.background, (0, 0))

        # ======================================
        # TÍTULO
        # ======================================

        title = self.title_font.render(

            TITLE,

            True,

            (255, 215, 0)

        )

        self.screen.blit(

            title,

            title.get_rect(

                center=(WIDTH // 2, 110)

            )

        )

        # ======================================
        # BOTÕES
        # ======================================

        mouse = pygame.mouse.get_pos()

        start_y = 260

        for i, option in enumerate(self.options):

            rect = pygame.Rect(

                WIDTH // 2 - 220,

                start_y + i * 85,

                440,

                60

            )

            if rect.collidepoint(mouse):

                self.selected = i

            color = (

                (240, 200, 40)

                if i == self.selected

                else

                (55, 55, 55)

            )

            pygame.draw.rect(

                self.screen,

                color,

                rect,

                border_radius=12

            )

            pygame.draw.rect(

                self.screen,

                (255, 255, 255),

                rect,

                3,

                border_radius=12

            )

            text = self.option_font.render(

                option,

                True,

                (255, 255, 255)

            )

            self.screen.blit(

                text,

                text.get_rect(

                    center=rect.center

                )

            )

        # ======================================
        # RODAPÉ
        # ======================================

        footer = self.footer_font.render(

            "Use ↑ ↓ ou o Mouse para navegar",

            True,

            (230, 230, 230)

        )

        self.screen.blit(

            footer,

            footer.get_rect(

                center=(WIDTH // 2, HEIGHT - 30)

            )

        )

        pygame.display.flip()

    # =====================================================

    def run(self):

        clock = pygame.time.Clock()

        while True:

            clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    return "quit"

                # ==================================
                # TECLADO
                # ==================================

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:

                        self.selected = (

                            self.selected - 1

                        ) % len(self.options)

                    elif event.key == pygame.K_DOWN:

                        self.selected = (

                            self.selected + 1

                        ) % len(self.options)

                    elif event.key == pygame.K_RETURN:

                        if self.selected == 0:

                            return "game"

                        elif self.selected == 1:

                            return "instructions"

                        elif self.selected == 2:

                            return "quit"

                # ==================================
                # MOUSE
                # ==================================

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        if self.selected == 0:

                            return "game"

                        elif self.selected == 1:

                            return "instructions"

                        elif self.selected == 2:

                            return "quit"

            self.draw()