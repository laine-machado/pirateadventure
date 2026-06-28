import pygame
from settings import *


class HUD:

    def __init__(self):

        # Fontes
        self.font = pygame.font.SysFont("Arial", 30, True)
        self.title_font = pygame.font.SysFont("Arial", 70, True)
        self.subtitle_font = pygame.font.SysFont("Arial", 40, True)

    # ==================================================
    # HUD DURANTE O JOGO
    # ==================================================

    def draw(self, screen, coins, goal, score, level):

        # Fundo do HUD
        painel = pygame.Surface((340, 110), pygame.SRCALPHA)
        painel.fill((0, 0, 0, 150))

        screen.blit(painel, (15, 15))

        # Fase
        fase = self.font.render(
            f"Fase: {level}",
            True,
            (255, 255, 0)
        )

        # Moedas
        moedas = self.font.render(
            f"Moedas: {coins}/{goal}",
            True,
            (255, 255, 255)
        )

        # Pontuação
        pontos = self.font.render(
            f"Pontuação: {score}",
            True,
            (0, 255, 0)
        )

        screen.blit(fase, (30, 25))
        screen.blit(moedas, (30, 55))
        screen.blit(pontos, (30, 85))

    # ==================================================
    # GAME OVER
    # ==================================================

    def draw_game_over(self, screen):

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(170)
        overlay.fill((0, 0, 0))

        screen.blit(overlay, (0, 0))

        titulo = self.title_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(
            titulo,
            titulo.get_rect(center=(WIDTH//2, HEIGHT//2-80))
        )

        texto = self.subtitle_font.render(
            "Pressione ENTER para reiniciar",
            True,
            (255, 255, 255)
        )

        screen.blit(
            texto,
            texto.get_rect(center=(WIDTH//2, HEIGHT//2+20))
        )

    # ==================================================
    # VITÓRIA
    # ==================================================

    def draw_victory(self, screen):

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(170)
        overlay.fill((0, 0, 0))

        screen.blit(overlay, (0, 0))

        titulo = self.title_font.render(
            "VOCÊ VENCEU!",
            True,
            (0, 255, 0)
        )

        screen.blit(
            titulo,
            titulo.get_rect(center=(WIDTH//2, HEIGHT//2-80))
        )

        texto = self.subtitle_font.render(
            "Pressione ENTER para voltar ao menu",
            True,
            (255, 255, 255)
        )

        screen.blit(
            texto,
            texto.get_rect(center=(WIDTH//2, HEIGHT//2+20))
        )

    # ==================================================
    # PAUSA
    # ==================================================

    def draw_pause(self, screen):

        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))

        screen.blit(overlay, (0, 0))

        titulo = self.title_font.render(
            "PAUSADO",
            True,
            (255, 255, 0)
        )

        screen.blit(
            titulo,
            titulo.get_rect(center=(WIDTH//2, HEIGHT//2))
        )