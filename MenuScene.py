import pygame as pg
from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

TOPLEFT=1
TOPRIGHT=2
BOTTOMLEFT=3
BOTTOMRIGHT=4
LEFT=5
RIGHT=6
TOP=7
BOTTOM=8
BODY=10

EDIT_MODE=True
#EDIT_MODE=False

class TextBox(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        DEBUG("<< Enter")
        super().__init__()
        self.text = "TextBox"
        self.font = pg.font.SysFont("굴림", 20)
        self.image = self.font.render(self.text, 1, pg.Color("White"))
        self.rect  = self.image.get_rect(topleft = (x, y))
        #self.surface = pg.Surface(self.size)
        #self.surface.fill(bg)
        DEBUG(" Exit>>")

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.image = self.font.render(text, 1, pg.Color("White"))
        self.rect = self.image.get_rect(topleft = (0, 0))
        #self.image.blit(self.text, (0, 0))
        #self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])

    def change_size(self, x, y, width, height):
        DEBUG("<< Enter")
        self.image = pg.transform.smoothscale(self.image, (width, height)) 
        self.rect  = self.image.get_rect(topleft = (x, y))
        DEBUG(" Exit>>")

    def update(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

class Board(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        DEBUG("<< Enter")
        super().__init__()
        #board_img  = pg.image.load('').convert_alpha()
        #board_img2 = pg.image.load('').convert_alpha()
        #self.font = pg.font.SysFont("Arial", 20)
        self.font = pg.font.SysFont("굴림", 20)
        self.board_img  = pg.Surface((width, height))
        self.board_img2 = pg.Surface((width, height))
        self.board_img.fill(RED)
        self.board_img2.fill(WHITE)
        self.board_imgs = [self.board_img, self.board_img2]
        self.board_index = 0
        #self.text = ""
        #self.over_img = pg.image.load('').convert_alpha()

        self.image = self.board_imgs[self.board_index]
        self.rect  = self.image.get_rect(topleft = (x, y))

        self.shadow = 2

        #self.over_sound = pg.mixer.Sound('audio/boad_over.mp3')
        #self.over_sound.set_volume(0.5)
        DEBUG(" Exit>>")

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pg.Color("White"))
        self.size = self.text.get_size()
        self.surface = pg.Surface(self.size)
        #self.surface.fill(bg)
        self.image.blit(self.text, (0, 0))
        #self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])

    def change_size(self, x, y, width, height):
        DEBUG("<< Enter")
        #self.image = pg.transform.smoothscale(self.image, (width, height)) 
        self.image = pg.transform.smoothscale(self.board_img, (width, height)) 
        self.rect  = self.image.get_rect(topleft = (x, y))
        DEBUG(" Exit>>")

    def board_input(self):
        DEBUG("<< Enter")
        keys = pg.key.get_pressed()
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed() == (1, 0, 0):
                INFO("Mouse Button pressed!! ")
            if keys[pg.K_SPACE]:
                INFO("Space key pressed!! ")
        DEBUG(" Exit>>")

    def apply_shadow(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def board_animation(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def update(self):
        DEBUG("<< Enter")
        self.board_input()
        self.apply_shadow()
        self.board_animation()
        DEBUG(" Exit>>")

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
        self.rectangle_draging = None
        self.linedrag_mode = None
        #Background 로딩
        #self.bg = SlideLeftBackground()
        #Clock 초기화
        self.clock = pg.time.Clock()
        DEBUG(" Exit>>")

    def start(self):
        DEBUG("<< Enter")
        DEBUG(">>>>>>>>>>>>>>>> [%s] Scene START >>>>>>>>>>>>>>>>"%(self.name))
        #게임 객체 로딩
        self.board = Board(0, 0, 400, 200)
        self.font_board = Board( 722, 2, 300, 500)
        self.text_box = TextBox( 0, 0, 300, 500)
        #그룹분리
        ## 전체 그룹에 추가
        self.allObjGroup = pg.sprite.Group()
        self.allObjGroup.add(self.board)
        self.allObjGroup.add(self.font_board)
        self.allObjGroup.add(self.text_box)

        for font in pg.font.get_fonts():
            INFO(f"font[{font}]")
            #self.font_board.font = font
            #self.font_board.change_text(f"[{font}]ABCabc가나다")
        #self.menu = pg.sprite.Group()
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
                    OnGoing = False

                if not EDIT_MODE:
                    INFO("RUNNING Mode")
                else:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        INFO("MOUSEBOTTONDOWN")
                        if event.button == 1:            
                            sprites = self.allObjGroup.sprites()
                            for sprite in sprites:
                                INFO("sprite founded!!")
                                INFO("sprite.rect = [{}]".format(sprite.rect))
                                INFO("eventpos = [{}]".format(event.pos))
                                if sprite.rect.collidepoint(event.pos):
                                    INFO("collision!!")
                                    self.drag_object = sprite
                                    mouse_x, mouse_y = event.pos
                                    mouse_rect = pg.Rect(mouse_x - 5, mouse_y - 5, 10, 10)
                                    # topleft check
                                    if   mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y)):
                                        self.linedrag_mode = TOPLEFT
                                        offset_x = sprite.rect.x - mouse_x
                                        offset_y = sprite.rect.y - mouse_y
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y)):
                                        self.linedrag_mode = TOPRIGHT
                                        offset_x = sprite.rect.x + sprite.rect.width - mouse_x
                                        offset_y = sprite.rect.y - mouse_y
                                    elif mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y + sprite.rect.height)):
                                        self.linedrag_mode = BOTTOMLEFT
                                        offset_x = sprite.rect.x - mouse_x
                                        offset_y = sprite.rect.y + sprite.rect.height - mouse_y
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height)):
                                        self.linedrag_mode = BOTTOMRIGHT
                                        offset_x = sprite.rect.x + sprite.rect.width - mouse_x
                                        offset_y = sprite.rect.y + sprite.rect.height - mouse_y
                                    elif (sprite.rect.x) < mouse_x < (sprite.rect.x + 5):
                                        self.linedrag_mode = LEFT
                                    elif (sprite.rect.x + sprite.rect.width - 5) < mouse_x < (sprite.rect.x + sprite.rect.width):
                                        self.linedrag_mode = RIGHT
                                    elif (sprite.rect.y) < mouse_y < (sprite.rect.y + 5):
                                        self.linedrag_mode = TOP
                                    elif (sprite.rect.y + sprite.rect.height - 5) < mouse_y < (sprite.rect.y + sprite.rect.height):
                                        self.linedrag_mode = BOTTOM
                                    else:
                                        self.linedrag_mode = BODY
                                        offset_x = sprite.rect.x - mouse_x
                                        offset_y = sprite.rect.y - mouse_y
                                        #self.rectangle_draging = True
                                    break
                    elif event.type == pg.MOUSEBUTTONUP:
                        if event.button == 1:            
                            #self.rectangle_draging = False
                            if self.drag_object != None:
                                INFO(f"self.drag_object.rect.pos=[ {self.drag_object.rect.x}, {self.drag_object.rect.y} ]")
                                INFO(f"self.drag_object.rect.size=[ {self.drag_object.rect.width}, {self.drag_object.rect.height} ]")
                            self.drag_object = None
                            self.linedrag_mode = None

                    elif event.type == pg.MOUSEMOTION:
                        INFO("self.linedrag_mode = [{}]".format(self.linedrag_mode))
                        mouse_x, mouse_y = event.pos
                        if self.linedrag_mode == None:
                            # Mouse Over 상황에서는 line drag를 할 수 있는 상황이면 마우스 커서의 모양을 바꾼다.
                            sprites = self.allObjGroup.sprites()
                            for sprite in sprites:
                                if sprite.rect.collidepoint(event.pos):
                                    #self.drag_object = sprite
                                    mouse_x, mouse_y = event.pos
                                    mouse_rect = pg.Rect(mouse_x - 5, mouse_y - 5, 10, 10)
                                    # topleft check
                                    if   mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y)):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y)):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                    elif mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y + sprite.rect.height)):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height)):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                    elif (sprite.rect.x) < mouse_x < (sprite.rect.x + 5):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                    elif (sprite.rect.x + sprite.rect.width - 5) < mouse_x < (sprite.rect.x + sprite.rect.width):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                    elif (sprite.rect.y) < mouse_y < (sprite.rect.y + 5):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                    elif (sprite.rect.y + sprite.rect.height - 5) < mouse_y < (sprite.rect.y + sprite.rect.height):
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                    else:
                                        #expected_cursor = pygame.cursors.Cursor(size, hotspot, xormask, andmask)
                                        #pygame.mouse.set_cursor(expected_cursor)
                                        #pg.cursors
                                        pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_ARROW)
                                else:
                                    pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_ARROW)
                        else:
                            if self.linedrag_mode == TOPLEFT:
                                DEBUG("TOPLEFT")
                                offset_width  = self.drag_object.rect.x - mouse_x
                                offset_height = self.drag_object.rect.y - mouse_y

                                DEBUG(f"[1]mouse_x  = [{mouse_x}]")
                                DEBUG(f"[1]mouse_y  = [{mouse_y}]")
                                DEBUG(f"[1]self.drag_object.rect.x  = [{self.drag_object.rect.x}]")
                                DEBUG(f"[1]self.drag_object.rect.y  = [{self.drag_object.rect.y}]")
                                DEBUG(f"[1]self.drag_object.rect.width   = [{self.drag_object.rect.width}]")
                                DEBUG(f"[1]self.drag_object.rect.height  = [{self.drag_object.rect.height}]")
                                DEBUG(f"[1]offset_width       = [{offset_width}]")
                                DEBUG(f"[1]offset_height      = [{offset_height}]")

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )

                                self.drag_object.rect.y      = mouse_y
                                self.drag_object.rect.x      = mouse_x
                            elif self.linedrag_mode == TOPRIGHT:
                                DEBUG("TOPRIGHT")
                                offset_width  = mouse_x - (self.drag_object.rect.x + self.drag_object.rect.width)
                                offset_height = self.drag_object.rect.y - mouse_y

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )

                                self.drag_object.rect.y      = mouse_y
                            elif self.linedrag_mode == BOTTOMLEFT:
                                DEBUG("BOTTOMLEFT")
                                offset_width  = self.drag_object.rect.x - mouse_x
                                offset_height = mouse_y - (self.drag_object.rect.y + self.drag_object.rect.height)

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )

                                self.drag_object.rect.x      = mouse_x
                            elif self.linedrag_mode == BOTTOMRIGHT:
                                DEBUG("BOTTOMRIGHT")
                                offset_width  = mouse_x - (self.drag_object.rect.x + self.drag_object.rect.width )
                                offset_height = mouse_y - (self.drag_object.rect.y + self.drag_object.rect.height)

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width,    # mouse_x - self.drag_object.rect.x
                                    self.drag_object.rect.height + offset_height    # mouse_y - self.drag_object.rect.y
                                )
                            elif self.linedrag_mode == TOP:
                                DEBUG("TOP")
                                offset_width  = 0
                                offset_height = self.drag_object.rect.y - mouse_y

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )

                                self.drag_object.rect.y      = mouse_y
                            elif self.linedrag_mode == BOTTOM:
                                DEBUG("BOTTOM")
                                offset_width  = 0
                                offset_height = mouse_y - (self.drag_object.rect.y + self.drag_object.rect.height)

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )
                            elif self.linedrag_mode == LEFT:
                                DEBUG("LEFT")
                                offset_width  = self.drag_object.rect.x - mouse_x
                                offset_height = 0

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )

                                self.drag_object.rect.x      = mouse_x
                            elif self.linedrag_mode == RIGHT:
                                DEBUG("RIGHT")
                                INFO(f"mouse_x = [{mouse_x}] , self.drag_object.rect.x = [{self.drag_object.rect.x}]")
                                offset_width  = mouse_x - (self.drag_object.rect.x + self.drag_object.rect.width)
                                offset_height = 0

                                self.drag_object.change_size(
                                    self.drag_object.rect.x, 
                                    self.drag_object.rect.y, 
                                    self.drag_object.rect.width  + offset_width, 
                                    self.drag_object.rect.height + offset_height
                                )
                            elif self.linedrag_mode == BODY:
                                INFO("BODY_DRAG")
                                self.drag_object.rect.x = mouse_x + offset_x
                                self.drag_object.rect.y = mouse_y + offset_y

                    #if event.type == pg.KEYDOWN:
                    #    DEBUG("event.type=[%d], event.key=[%d]"%(event.type, event.key))
                        #키보드 제어권 전달
                    #    if event.key == pg.K_SPACE:
                    #        OnGoing = False

                    #if event.type == pg.MOUSEBUTTONDOWN:
                    #    INFO("event.type=[%d], event.key=[%d]"%(event.type, event.key))
            # 배경 초기화
            self.gamepad.fill(WHITE)
            # 배경 그리기
            self.bg.update(self.gamepad)
            # 객체 그리기
            self.allObjGroup.draw(self.gamepad)
            self.allObjGroup.update()
            # 디스플레이 업데이트
            pg.display.update()
            # refresh rate 보정
            self.clock.tick(REFRESH_RATE)

        DEBUG("**********************goto next Scene = [%s]"%self.nextScene)
        DEBUG(" Exit>>")
        return self.nextScene

if __name__ == '__main__':
    pg.init()
    gamepad = pg.display.set_mode(GAME_SCREEN)
    menuScene = MenuScene("menu", gamepad)
    menuScene.start()
    pg.quit()
