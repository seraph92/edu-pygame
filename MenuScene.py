import pygame as pg
from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

class MenuScene(Scene):
    def __init__(self, name, gamepad):
        DEBUG("<< Enter")
        Scene.__init__(self, name)
        self.name = name
        self.gamepad = gamepad
        #Background 로딩
        #self.bg = SlideLeftBackground()
        #Clock 초기화
        self.clock = pg.time.Clock()
        DEBUG(" Exit>>")

    def start(self):
        DEBUG("<< Enter")
        DEBUG(">>>>>>>>>>>>>>>> [%s] Scene START >>>>>>>>>>>>>>>>"%(self.name))
        #게임 객체 로딩
        #Background 로딩
        self.bg = MenuBackground()
        #Event Loop 진입
        nextScene = self.event_loop()
        DEBUG(" Exit>>")
        return nextScene

    def event_loop(self):
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

        nextScene = "Stage1"
        DEBUG(" Exit>>")
        return nextScene

