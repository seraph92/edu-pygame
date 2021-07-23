import pygame as pg
from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

import pygame_menu as pgm
from pygame_menu.examples import create_example_window

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

    def set_difficulty(selected, value):
        """
        Set the difficulty of the game.
        :return: None
        """
        print('Set difficulty to {} ({})'.format(selected[0], value))

    def start_the_game(self):
        """
        Function that starts a game. This is raised by the menu button,
        here menu can be disabled, etc.
        :return: None
        """
        self.user_name
        print('{0}, Do the job here!'.format(self.user_name.get_value()))

    def draw_background(self):
        self.bg.update(self.gamepad)

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

        # surface = create_example_window('Example - Simple', (600, 400))

        menu = pgm.Menu(
          height=300,
          theme=pgm.themes.THEME_BLUE,
          title='Welcome',
          width=400
        )

        user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
        menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty)
        menu.add.button('Play', self.start_the_game)
        menu.add.button('Quit', pgm.events.EXIT)

        DEBUG("<< Enter")
        '''
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

        '''
        menu.mainloop(self.gamepad, self.draw_background)
        #menu.mainloop(self.gamepad, self.draw_background, disable_loop=True, fps_limit=60)
        #main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        nextScene = "Stage1"
        DEBUG(" Exit>>")
        return nextScene

