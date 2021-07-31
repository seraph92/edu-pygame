import pygame as pg
import pygame.freetype
import pygame.gfxdraw

from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

import typing

TOPLEFT=1
TOPRIGHT=2
BOTTOMLEFT=3
BOTTOMRIGHT=4
LEFT=5
RIGHT=6
TOP=7
BOTTOM=8
BODY=10

#EDIT_MODE=True
EDIT_MODE=False

class UIComponent:
    seed = 100

    def __init__(self):
        DEBUG("<< Enter")
        INFO("UIComponent init")
        # 일련번호 할당
        self.__ou_id = UIComponent.__gen_id__()
        INFO(f"__ou_id = {self.__ou_id}")
        self.on_click=None
        DEBUG(" Exit>>")

    def get_ou_id(self):
        return self.__ou_id

    @classmethod
    def __gen_id__(cls):
        cls.seed = cls.seed + 1
        return cls.seed


    def onClick(self, event):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def onOver(self, event):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

class Label(pg.sprite.DirtySprite, UIComponent):
    def __init__(self, text, pos):
        DEBUG("<< Enter")
        super().__init__()
        UIComponent.__init__(self)
        self.text = text
        self.font_name = "malgungothic"
        self.font_size = 30
        self.color = pg.Color("White")

        self.font = pygame.freetype.SysFont(self.font_name, self.font_size)

        ( self.text_image, self.text_rect ) = self.font.render(self.text, self.color)
        INFO(f"self.text_image = [{self.text_image}]")
        INFO(f"type of self.text_image = [{type(self.text_image)}]")

        self.image = pg.Surface([self.text_rect.width, self.text_rect.height], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(self.text_image, (0, 0))
        self.rect  = self.image.get_rect()

        self.rect.x, self.rect.y = pos

        self.rel_width  = self.rect.width
        self.rel_height = self.rect.height
        DEBUG(" Exit>>")

    def change_font(self, font_name):
        self.font_name = font_name

    def change_text(self, text):
        """Change the text whe you click"""
        self.text = text
        self.font = pygame.freetype.SysFont(self.font_name, self.font_size)
        ( self.text_image, self.text_rect ) = self.font.render(self.text, self.color)
        
        self.image = pg.transform.smoothscale(self.text_image, (self.rel_width, self.rel_height))
        self.rect  = self.image.get_rect(topleft = (self.rect.x, self.rect.y))

    def change_size(self, x, y, width, height):
        DEBUG("<< Enter")
        self.rel_x = x
        self.rel_y = y

        if width  < 1: width  = 0
        if height < 1: height = 0
        
        self.rel_width  = width
        self.rel_height = height

        self.image = pg.transform.smoothscale(self.text_image, (width, height)) 
        self.rect  = self.image.get_rect(topleft = (x, y))
        self.rect.x = x
        self.rect.y = y
        self.rect.width  = width
        self.rect.height = height
        DEBUG(" Exit>>")

    def board_input(self):
        DEBUG("<< Enter")
        keys = pg.key.get_pressed()
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed() == (1, 0, 0):
                INFO("Mouse Button pressed!! ")
                self.change_text("마우스 눌렀어.")
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
        self.dirty = 1
        self.board_input()
        self.apply_shadow()
        self.board_animation()
        DEBUG(" Exit>>")

class Button(pg.sprite.DirtySprite, UIComponent):
    def __init__(self, text,  pos, bg="black", action=None):
        DEBUG("<< Enter")
        INFO("Button init")
        super().__init__()
        UIComponent.__init__(self)
        self.on_click = None
        self.all_group = None
        self.text = text
        self.font_name = "malgungothic"
        self.font_size = 30
        self.color = pg.Color("White")
        self.x, self.y = pos

        self.font = pygame.freetype.SysFont(self.font_name, self.font_size)

        ( tmp_image, tmp_rect ) = self.font.render("밝", self.color)
        one_width  = int(tmp_rect.width * 1.36)
        one_height = int(tmp_rect.height * 1.83)

        self.margin_width = one_width
        self.margin_height = (one_height -tmp_rect.height) // 2

        ( self.text_image, self.text_rect ) = self.font.render(self.text, self.color)

        INFO(f"self.text_image = [{self.text_image}]")
        INFO(f"type of self.text_image = [{type(self.text_image)}]")

        self.image = pg.Surface([self.text_rect.width + (self.margin_width*2), self.text_rect.height + (self.margin_height*2)], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect  = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.draw_rounded_rect(self.image, pg.Rect(0, 0, self.rect.width, self.rect.height), RED, 10)

        #self.image.fill(bg)
        self.image.blit(self.text_image, (self.margin_width, self.margin_height))
        self.rel_width  = self.rect.width
        self.rel_height = self.rect.height

        #self.change_text(text, bg)
        DEBUG(" Exit>>")

    def add(self, group):
        super().add(group)
        if self.all_group == None:
            self.all_group = group

    def handle_input(self):
        DEBUG("<< Enter")
        keys = pg.key.get_pressed()
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed() == (1, 0, 0):
                INFO(f"[{self.get_ou_id()}-Button]Mouse Button pressed!! ")
                INFO(f"[{self.get_ou_id()}-self.on_click[{self.on_click}] ")
                if self.on_click != None:
                    INFO(f"[{self.get_ou_id()}]self.on_click()")
                    self.on_click()
            if keys[pg.K_SPACE]:
                INFO("Space key pressed!! ")
        DEBUG(" Exit>>")

    def update(self):
        DEBUG("<< Enter")
        #self.handle_input()
        DEBUG(" Exit>>")

    def setOnClick(self, f):
        DEBUG("<< Enter")
        INFO(f"on_cick_assign = [{f}]")
        self.on_click = f
        DEBUG(" Exit>>")

    def change_text(self, text, bg="black"):
        DEBUG("<< Enter")
        """Change the text when you click"""
        self.text = text
        self.font = pygame.freetype.SysFont(self.font_name, self.font_size)
        ( self.text_image, self.text_rect ) = self.font.render(self.text, self.color)
        
        self.image = pg.Surface([self.rect.width, self.rect.height], pg.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.fill(bg)
        self.image.blit(self.text_image, (0, 0))
        self.rect  = self.image.get_rect()
        DEBUG(" Exit>>")

    def draw_rounded_rect(self, surface, rect, color, corner_radius):
        ''' Draw a rectangle with rounded corners.
        Would prefer this: 
            pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
        but this option is not yet supported in my version of pygame so do it ourselves.

        We use anti-aliased circles to make the corners smoother
        '''
        if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
            raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)


    def draw_bordered_rounded_rect(self, surface, rect, color, border_color, corner_radius, border_thickness):
        if corner_radius < 0:
            raise ValueError(f"border radius ({corner_radius}) must be >= 0")

        rect_tmp = pygame.Rect(rect)
        center = rect_tmp.center

        if border_thickness:
            if corner_radius <= 0:
                pygame.draw.rect(surface, border_color, rect_tmp)
            else:
                self.draw_rounded_rect(surface, rect_tmp, border_color, corner_radius)

            rect_tmp.inflate_ip(-2*border_thickness, -2*border_thickness)
            inner_radius = corner_radius - border_thickness + 1
        else:
            inner_radius = corner_radius

        if inner_radius <= 0:
            pygame.draw.rect(surface, color, rect_tmp)
        else:
            self.draw_rounded_rect(surface, rect_tmp, color, inner_radius) 

    def show(self):
        DEBUG("<< Enter")
        #screen.blit(button1.surface, (self.x, self.y))
        DEBUG(" Exit>>")
 

class Board(pg.sprite.DirtySprite, UIComponent):
    def __init__(self, x, y, width, height, bg=GRAY):
        DEBUG("<< Enter")
        super().__init__()
        UIComponent.__init__(self)
        #board_img  = pg.image.load('').convert_alpha()
        #board_img2 = pg.image.load('').convert_alpha()
        #self.font = pg.font.SysFont("Arial", 20)
        self.font = pg.font.SysFont("굴림", 20)
        self.bg = bg
        self.board_img  = pg.Surface((width, height))
        self.board_img2 = pg.Surface((width, height))
        self.board_img.fill(self.bg)
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
        if width  < 1: width  = 0
        if height < 1: height = 0
        self.image = pg.transform.smoothscale(self.board_img, (width, height)) 
        self.rect  = self.image.get_rect(topleft = (x, y))
        DEBUG(" Exit>>")

    def handle_input(self):
        DEBUG("<< Enter")
        keys = pg.key.get_pressed()
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed() == (1, 0, 0):
                INFO(f"[{self.get_ou_id()}-Board]Mouse Button pressed!! ")
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
        self.dirty = 1
        #self.handle_input()
        self.apply_shadow()
        self.board_animation()
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
        self.onGoing = True
        #Background 로딩
        #self.bg = SlideLeftBackground()
        #Clock 초기화
        self.clock = pg.time.Clock()
        DEBUG(" Exit>>")

    def gotoStage(self, stage, onGoing):
        self.nextScene = stage
        self.onGoing = onGoing

##    def quit(self):
##        self.nextScene = ""
##        self.onGoing = False
##
##    def gotoStage1(self):
##        self.nextScene = "Stage1"
##        self.onGoing = False

    def start(self):
        DEBUG("<< Enter")
        DEBUG(">>>>>>>>>>>>>>>> [%s] Scene START >>>>>>>>>>>>>>>>"%(self.name))
        #게임 객체 로딩
        self.board = Board(219, 41, 585, 407, DARKOLIVEGREEN)
        self.menu_title = Label("메뉴를 선택해 주세요.", (348, 63))
        self.exit_button = Button("종 료", (447, 348), WHITE)
        self.play_button = Button("PLAY", (447, 227), WHITE)
        # 정렬
        self.menu_title.rect.centerx = self.board.rect.centerx
        self.exit_button.rect.centerx = self.board.rect.centerx
        self.menu_title.rect.centerx = self.board.rect.centerx
        #그룹분리
        ## 전체 그룹에 추가
        self.allObjGroup = pg.sprite.Group()
        self.board.add(self.allObjGroup)
        self.menu_title.add(self.allObjGroup)
        self.exit_button.add(self.allObjGroup)
        self.play_button.add(self.allObjGroup)
        #self.allObjGroup.add(self.board)
        #self.allObjGroup.add(self.menu_title)
        #self.allObjGroup.add(self.exit_button)
        #self.allObjGroup.add(self.play_button)

        #self.exit_button.setOnClick(self.quit)
        #self.play_button.setOnClick(self.gotoStage1)
        self.exit_button.setOnClick(lambda stage="", onGoing=False : self.gotoStage(stage, onGoing))
        self.play_button.setOnClick(lambda stage="Stage1", onGoing=False : self.gotoStage(stage, onGoing))
        

        #for font in pg.font.get_fonts():
        #    INFO(f"font[{font}]")
            #self.font_board.font = font
            #self.font_board.change_text(f"[{font}]ABCabc가나다")
        #self.menu = pg.sprite.Group()
        #Background 로딩
        self.bg = MenuBackground()
        #Event Loop 진입
        self.nextScene = self.event_loop()
        INFO(f"self.nextScene = [{self.nextScene}]")
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
        self.onGoing = True
        while self.onGoing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.onGoing = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.onGoing = False

                if not EDIT_MODE:
                    INFO("RUNNING Mode")
                    if event.type == pg.MOUSEBUTTONDOWN:
                        INFO("MOUSEBOTTONDOWN")
                        if event.button == 1:            
                            sprites = self.allObjGroup.sprites()
                            for sprite in reversed(sprites):
                                INFO("sprite founded!!")
                                INFO("sprite.rect = [{}]".format(sprite.rect))
                                INFO("eventpos = [{}]".format(event.pos))
                                if sprite.rect.collidepoint(event.pos):
                                    INFO("collision!!")
                                    self.drag_object = sprite
                                    break
                            self.drag_object.handle_input()
 
                else:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        INFO("MOUSEBOTTONDOWN")
                        if event.button == 1:            
                            sprites = self.allObjGroup.sprites()
                            for sprite in reversed(sprites):
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
                                self.drag_object.onClick(event.pos)
                            self.drag_object = None
                            self.linedrag_mode = None

                    elif event.type == pg.MOUSEMOTION:
                        INFO("self.linedrag_mode = [{}]".format(self.linedrag_mode))
                        mouse_x, mouse_y = event.pos
                        if self.linedrag_mode == None:
                            # Mouse Over 상황에서는 line drag를 할 수 있는 상황이면 마우스 커서의 모양을 바꾼다.
                            sprites = self.allObjGroup.sprites()
                            for sprite in reversed(sprites):
                                if sprite.rect.collidepoint(event.pos):
                                    INFO(f"Motion Collisiton detected!!")
                                    #self.drag_object = sprite
                                    mouse_x, mouse_y = event.pos
                                    mouse_rect = pg.Rect(mouse_x - 5, mouse_y - 5, 10, 10)
                                    # topleft check
                                    if   mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y)):
                                        INFO(f"Drag Mouse Cursor = 11h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y)):
                                        INFO(f"Drag Mouse Cursor = 1h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                    elif mouse_rect.collidepoint((sprite.rect.x, sprite.rect.y + sprite.rect.height)):
                                        INFO(f"Drag Mouse Cursor = 7h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENESW)
                                    elif mouse_rect.collidepoint((sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height)):
                                        INFO(f"Drag Mouse Cursor = 5h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENWSE)
                                    elif (sprite.rect.x) < mouse_x < (sprite.rect.x + 5):
                                        INFO(f"Drag Mouse Cursor = 9h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                    elif (sprite.rect.x + sprite.rect.width - 5) < mouse_x < (sprite.rect.x + sprite.rect.width):
                                        INFO(f"Drag Mouse Cursor = 3h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZEWE)
                                    elif (sprite.rect.y) < mouse_y < (sprite.rect.y + 5):
                                        INFO(f"Drag Mouse Cursor = 12h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                    elif (sprite.rect.y + sprite.rect.height - 5) < mouse_y < (sprite.rect.y + sprite.rect.height):
                                        INFO(f"Drag Mouse Cursor = 6h")
                                        #pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_SIZENS)
                                    else:
                                        #expected_cursor = pygame.cursors.Cursor(size, hotspot, xormask, andmask)
                                        #pygame.mouse.set_cursor(expected_cursor)
                                        # body grab
                                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                                    break
                                else:
                                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
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
                    #        self.onGoing = False

                    #if event.type == pg.MOUSEBUTTONDOWN:
                    #    INFO("event.type=[%d], event.key=[%d]"%(event.type, event.key))
            # 배경 초기화
            self.gamepad.fill(WHITE)
            # 배경 그리기
            self.bg.update(self.gamepad)
            # 객체 이벤트 처리
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
