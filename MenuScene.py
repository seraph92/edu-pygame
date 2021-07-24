import pygame as pg
from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

#import pygame_menu as pgm
#from pygame_menu.examples import create_example_window

class Button:
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        DEBUG("<< Enter")
        self.x, self.y = pos
        self.font = pg.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
        DEBUG(" Exit>>")

    def change_text(self, text, bg="black"):
        DEBUG("<< Enter")
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pg.Color("White"))
        self.size = self.text.get_size()
        self.surface = pg.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        DEBUG(" Exit>>")
 
    def show(self):
        DEBUG("<< Enter")
        screen.blit(button1.surface, (self.x, self.y))
        DEBUG(" Exit>>")
 
    def click(self, event):
        DEBUG("<< Enter")
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
        DEBUG(" Exit>>")


class MenuScene(Scene):
    def __init__(self, name, gamepad):
        DEBUG("<< Enter")
        Scene.__init__(self, name)
        self.name = name
        self.gamepad = gamepad
        self.nextScene = ""
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
        self.nextScene = self.event_loop()
        DEBUG(" Exit>>")
        return self.nextScene

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

        DEBUG("**********************goto next Scene = [%s]"%self.nextScene)
        DEBUG(" Exit>>")
        return self.nextScene

