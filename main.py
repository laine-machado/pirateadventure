import pygame

from settings import *
from menu import Menu
from game import Game


# ======================================================
# TELA DE INSTRUÇÕES
# ======================================================

def instructions(screen):

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("Arial", 60, True)
    subtitle_font = pygame.font.SysFont("Arial", 38, True)
    font = pygame.font.SysFont("Arial", 30)

    # =====================================
    # IMAGEM DE FUNDO
    # =====================================

    background = pygame.image.load(
        "assets/images/menu_background.png"
    ).convert()

    background = pygame.transform.smoothscale(
        background,
        (WIDTH, HEIGHT)
    )

    while True:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_RETURN:
                    return

        # =====================================
        # FUNDO
        # =====================================

        screen.blit(background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))  # Quanto maior o último valor, mais escuro
        screen.blit(overlay, (0, 0))

        # =====================================
        # TÍTULO
        # =====================================

        title = title_font.render(

            "INSTRUÇÕES",

            True,

            (255, 215, 0)

        )

        screen.blit(

            title,

            title.get_rect(

                center=(WIDTH//2, 80)

            )

        )

        # =====================================
        # OBJETIVO
        # =====================================

        objetivo = subtitle_font.render(

            "Objetivo",

            True,

            (0,255,255)

        )

        screen.blit(objetivo, (80,170))

        texto = font.render(

            "Colete moedas para passar de fase enquanto desvia dos inimigos.",

            True,

            (255,255,255)

        )

        screen.blit(texto, (80,220))

        # =====================================
        # CONTROLES
        # =====================================

        controle = subtitle_font.render(

            "Controles",

            True,

            (0,255,255)

        )

        screen.blit(controle, (80,330))

        controles = [

            "←  Move para a esquerda",

            "→  Move para a direita",

            "ESPAÇO  Pula"

        ]

        y = 390

        for linha in controles:

            txt = font.render(

                linha,

                True,

                (255,255,255)

            )

            screen.blit(txt, (120,y))

            y += 45

        # =====================================
        # VOLTAR
        # =====================================

        voltar = font.render(

            "ENTER ou ESC para voltar ao Menu",

            True,

            (255,255,0)

        )

        screen.blit(

            voltar,

            voltar.get_rect(

                center=(WIDTH//2, HEIGHT-50)

            )

        )

        pygame.display.flip()


# ======================================================
# MAIN
# ======================================================

def main():

    pygame.init()

    screen = pygame.display.set_mode(

        (WIDTH, HEIGHT)

    )

    pygame.display.set_caption(TITLE)

    state = "menu"

    while True:

        # =====================================
        # MENU
        # =====================================

        if state == "menu":

            menu = Menu(screen)

            state = menu.run()

        # =====================================
        # JOGO
        # =====================================

        elif state == "game":

            game = Game(screen)

            state = game.run()

        # =====================================
        # INSTRUÇÕES
        # =====================================

        elif state == "instructions":

            instructions(screen)

            state = "menu"

        # =====================================
        # SAIR
        # =====================================

        elif state == "quit":

            break

    pygame.quit()


# ======================================================

if __name__ == "__main__":

    main()