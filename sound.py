import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'w_pistol.wav' )
        self.npc_pain = pg.mixer.Sound(self.path + 'n_brown_spotted.ogg')
        self.npc_death = pg.mixer.Sound(self.path + 'n_blue_death.ogg')
        self.npc_shot = pg.mixer.Sound(self.path + 'n_soldier_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'p_hurt.ogg')
        self.theme = pg.mixer.music.load(self.path + 'theme.ogg')
        pg.mixer.music.set_volume(0.3)