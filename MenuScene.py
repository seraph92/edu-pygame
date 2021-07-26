import pygame as pg
from setting  import *
from Background import *
from BKLOG import *
from Scenes import *

TOPLEFT=1
TOPRIGHT=2
BOTTOMLEFT=3
BOTTOMRIGHT=4
BODY=5


#import pygame_menu as pgm
#from pygame_menu.examples import create_example_window

class Board(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        DEBUG("<< Enter")
        super().__init__()
        #board_img  = pg.image.load('').convert_alpha()
        #board_img2 = pg.image.load('').convert_alpha()
        self.board_img  = pg.Surface((width, height))
        self.board_img2 = pg.Surface((width, height))
        self.board_img.fill(RED)
        self.board_img2.fill(WHITE)
        self.board_imgs = [self.board_img, self.board_img2]
        self.board_index = 0
        #self.over_img = pg.image.load('').convert_alpha()

        self.image = self.board_imgs[self.board_index]
        self.rect  = self.image.get_rect(topleft = (x, y))

        self.shadow = 2

        #self.over_sound = pg.mixer.Sound('audio/boad_over.mp3')
        #self.over_sound.set_volume(0.5)
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
        #그룹분리
        self.menu = pg.sprite.Group()
        self.menu.add(self.board)
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
                elif event.type == pg.MOUSEBUTTONDOWN:
                    INFO("MOUSEBOTTONDOWN")
                    if event.button == 1:            
                        sprites = self.menu.sprites()
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
                                else:
                                    self.linedrag_mode = BODY
                                    offset_x = sprite.rect.x - mouse_x
                                    offset_y = sprite.rect.y - mouse_y
                                    #self.rectangle_draging = True
                                break
                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:            
                        #self.rectangle_draging = False
                        self.drag_object = None
                        self.linedrag_mode = None

                elif event.type == pg.MOUSEMOTION:
                    #INFO("self.rectangle_draging = [{}]".format(self.rectangle_draging))
                    INFO("self.linedrag_mode = [{}]".format(self.linedrag_mode))
                    mouse_x, mouse_y = event.pos
                    #if self.rectangle_draging:
                    #    self.drag_object.rect.x = mouse_x + offset_x
                    #    self.drag_object.rect.y = mouse_y + offset_y
                    if self.linedrag_mode:
                        #offset_width  = self.drag_object.rect.x - ( mouse_x + offset_x )
                        #offset_height = self.drag_object.rect.y - ( mouse_y + offset_y )
                        #INFO("mouse_x       = [{}]".format(mouse_x))
                        #INFO("mouse_y       = [{}]".format(mouse_y))
                        #INFO("offset_x      = [{}]".format(offset_x))
                        #INFO("offset_y      = [{}]".format(offset_y))
                        #INFO("self.drag_object.rect.x = [{}]".format(self.drag_object.rect.x))
                        #INFO("self.drag_object.rect.y = [{}]".format(self.drag_object.rect.y))
                        #INFO("offset_width  = [{}]".format(offset_width))
                        #INFO("offset_height = [{}]".format(offset_height))
                        if self.linedrag_mode == TOPLEFT:
                            INFO("TOPLEFT")
                            self.drag_object.rect.x      = mouse_x + offset_x
                            self.drag_object.rect.y      = mouse_y + offset_y
                            self.drag_object.rect.inflate_ip( offset_width, offset_height )
                            #self.drag_object.rect.width  -= mouse_x + offset_x
                            #self.drag_object.rect.height -= mouse_y + offset_y
                        elif self.linedrag_mode == TOPRIGHT:
                            INFO("TOPRIGHT")
                            #self.drag_object.rect.x      = mouse_x + offset_x
                            self.drag_object.rect.y      = mouse_y + offset_y
                            self.drag_object.rect.inflate_ip( -offset_width, offset_height )
                            #self.drag_object.rect.width  -= mouse_x + offset_x
                            #self.drag_object.rect.height -= mouse_y + offset_y
                        elif self.linedrag_mode == BOTTOMLEFT:
                            INFO("BOTTOMLEFT")
                            self.drag_object.rect.x      = mouse_x + offset_x
                            #self.drag_object.rect.y      = mouse_y + offset_y
                            self.drag_object.rect.inflate_ip( offset_width, -offset_height )
                            #self.drag_object.rect.width  -= mouse_x + offset_x
                            #self.drag_object.rect.height -= mouse_y + offset_y
                        elif self.linedrag_mode == BOTTOMRIGHT:
                            INFO("BOTTOMRIGHT")
                            offset_width  = self.drag_object.rect.x + self.drag_object.rect.width  - (mouse_x)
                            offset_height = self.drag_object.rect.y + self.drag_object.rect.height - (mouse_y)
                            #self.drag_object.rect.x      = mouse_x + offset_x
                            #self.drag_object.rect.y      = mouse_y + offset_y
                            INFO("offset_width       = [{}]".format(offset_width))
                            INFO("offset_height      = [{}]".format(offset_height))
                            self.drag_object.rect.inflate_ip( -offset_width, -offset_height )
                            #self.drag_object.rect.width  -= mouse_x + offset_x
                            #self.drag_object.rect.height -= mouse_y + offset_y
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
            self.menu.draw(self.gamepad)
            self.menu.update()
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
