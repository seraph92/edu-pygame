import pygame as pg
from setting  import *

from BKLOG import *

class Game:
    """
    game class
    """
    #gamepad
    def init(self):
        DEBUG("<< Enter")
        #pygame.init()
        DEBUG("PG_INIT : ")
        pg.init()

        #디스플레이 초기화
        DEBUG("GAME_SCREEN : " + GAME_SCREEN)
        self.gamepad = pg.display.set_mode(GAME_SCREEN)
        DEBUG("GAME_TITLE : " + GAME_TITLE)
        pg.display.set_caption(GAME_TITLE)

        #게임 객체 로딩
        #Background 로딩
        #Sound 로딩
        #Clock 초기화
        DEBUG(" Exit>>")


    def __init__(self):
        DEBUG("<< Enter")
        self.init(self)
        self.event_loop(self)
        DEBUG(" Exit>>")

    def event_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    break
