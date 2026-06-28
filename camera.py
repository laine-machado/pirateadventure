from settings import *


class Camera:

    def __init__(self, world_width):

        self.world_width = world_width

        # Posição atual da câmera
        self.x = 0

        # Quanto menor, mais suave será a câmera
        self.smoothness = 0.10

    # =========================================

    def update(self, player):

        # Centro desejado da câmera
        target_x = player.rect.centerx - WIDTH // 2

        # Movimento suave
        self.x += (target_x - self.x) * self.smoothness

        # Limites do mapa
        if self.x < 0:
            self.x = 0

        max_x = self.world_width - WIDTH

        if self.x > max_x:
            self.x = max_x

    # =========================================

    def get_offset(self):

        return int(self.x)