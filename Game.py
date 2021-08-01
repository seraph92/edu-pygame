import pygame as pg
from setting  import *

from BKLOG import *
from Background import *

from Scenes import *
from MenuScene import *
from Stage1Scene import *

class Game:
    """
    game class
    """
    #background = None
    gamepad = None

    def init(self):
        DEBUG("<< Enter")
        #pygame.init()
        DEBUG("PG_INIT : ")
        pg.init()

        #디스플레이 초기화
        DEBUG("GAME_SCREEN : " + str(GAME_SCREEN))
        self.gamepad = pg.display.set_mode(GAME_SCREEN)
        DEBUG("GAME_TITLE : " + GAME_TITLE)
        pg.display.set_caption(GAME_TITLE)

        # Scene 로딩
        self.scenes = Scenes()
        self.scenes.addScene("Home", MenuScene("Home", self.gamepad))
        self.scenes.addScene("Stage1", Stage1Scene("Stage1", self.gamepad))
        DEBUG("SCENES STATUS = [%s]"%self.scenes.status())
        #Sound 로딩
        #Clock 초기화
        DEBUG(" Exit>>")

    def __init__(self):
        DEBUG("<< Enter")
        self.init()
        nextScene = "Home"
        while nextScene:
            if nextScene:
                nextScene = self.scenes.start(nextScene)

        DEBUG("SCENE STATUS = [%s]"%nextScene)
        DEBUG(" Exit>>")

if __name__ == '__main__':
    Game()