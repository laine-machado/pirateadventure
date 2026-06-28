from settings import *


class Level:

    def __init__(self):

        self.current = 1

        self.levels = {

            1: {

                "background": "assets/images/fase1.png",

                "goal": 20,

                "enemy_speed": (4, 6),

                "max_enemies": 3,

                "spawn_time": (80, 180)

            },

            2: {

                "background": "assets/images/fase2.png",

                "goal": 30,

                "enemy_speed": (5, 7),

                "max_enemies": 4,

                "spawn_time": (60, 140)

            },

            3: {

                "background": "assets/images/fase3.png",

                "goal": 50,

                "enemy_speed": (5, 6),

                "max_enemies": 3,

                "spawn_time": (80, 140)

            }

        }

        self.load()

    # =====================================

    def load(self):

        data = self.levels[self.current]

        self.background = data["background"]

        self.goal = data["goal"]

        self.enemy_speed = data["enemy_speed"]

        self.max_enemies = data["max_enemies"]

        self.spawn_time = data["spawn_time"]

    # =====================================

    def next_level(self):

        if self.current < 3:

            self.current += 1

            self.load()

            return True

        return False

    # =====================================

    def reset(self):

        self.current = 1

        self.load()