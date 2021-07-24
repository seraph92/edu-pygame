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

        #게임 객체 로딩
        #Background 로딩
        #self.bg = SlideLeftBackground()
        # Scene 로딩
        self.scenes = Scenes()
        self.scenes.addScene("Home", MenuScene("Home", self.gamepad))
        self.scenes.addScene("Stage1", Stage1Scene("Stage1", self.gamepad))
        DEBUG("SCENES STATUS = [%s]"%self.scenes.status())
        #Sound 로딩
        #Clock 초기화
        #self.clock = pg.time.Clock()
        DEBUG(" Exit>>")

    def __init__(self):
        DEBUG("<< Enter")
        self.init()
        #scene = self.scenes.start("Home")
        #DEBUG("SCENES STATUS = [%s]"%self.scenes.status())
        #DEBUG("SCENE STATUS = [%s]"%scene.status())
        nextScene = "Home"
        while nextScene:
            if nextScene:
                nextScene = self.scenes.start(nextScene)

        DEBUG("SCENE STATUS = [%s]"%nextScene)
        #self.event_loop()
        DEBUG(" Exit>>")

    def event_loop(self):   #### 현재 사용하지 않음
        '''
        IF event.type == pygame.QUIT
            break
        IF event.type == pygame.KEYDOWN
            키보드 제어권 전달
        
        배경초기화
        배경그리기
        객체 그리기

        디스플레이 업데이트 # pygame.display.update()
        refresh rate 보정 # clock.tick(60)

        pygame.quit()
        quit() # 종료
        '''
        DEBUG("<< Enter")
        OnGoing = True
        while OnGoing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    break
                if event.type == pg.KEYDOWN:
                    DEBUG("event.type=[%d], event.key=[%d]"%(event.type, event.key))
                    #키보드 제어권 전달
                    if event.key == pg.K_SPACE:
                        OnGoing = False

            # 배경 초기화
            self.gamepad.fill(WHITE)
            # 배경 그리기
            self.bg.update(self.gamepad)
            # 객체 그리기
            # 디스플레이 업데이트
            pg.display.update()
            # refresh rate 보정
            self.clock.tick(REFRESH_RATE)

        DEBUG(" Exit>>")

if __name__ == '__main__':
    Game()