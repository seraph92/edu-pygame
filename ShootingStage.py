__author__ = "seraph92@gmail.com"
from setting import *
from BKLOG import *

import pygame as pg
import pygame.freetype
import pygame.gfxdraw

from Background import *
from Scenes import *

from time import sleep
import random
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

EDIT_MODE = False

class AirScraft(pg.sprite.DirtySprite):
    def __init__(self, resource_id, size=None):
        DEBUG("<< Enter")
        super().__init__()
        self.image = pg.image.load(IMG_PATH + '/' + OBJ_IMG_FILE[resource_id])
        #self.image = self.image.convert_alpha()
        self.rect  = self.image.get_rect()
        self.play_rect = None

        if size:
            INFO("size에 맞게 크기 조절")
            INFO(f"size = [{size}]")
            INFO(f"rect = [{self.rect.width}, {self.rect.height}]")
            # Get Ratio
            #ratio = self.rect.height / self.rect.width   ### height / width
            candidates = []
            #candidates.append((size[0], size[1] * ratio))
            #candidates.append((size[0] / ratio, size[1]))
            candidates.append((size[0], size[1] * self.rect.height // self.rect.width))
            candidates.append((size[0] * self.rect.width // self.rect.height, size[1]))

            for candi in candidates:
                INFO(f"candi = [{candi}]")
                INFO(f"candi(int) = [{int(candi[0])}, {int(candi[1])}")
                if candi[0] <= size[0] and candi[1] <= size[1]:
                    self.image = pg.transform.scale(self.image, (int(candi[0]), int(candi[1])))
                    self.rect = self.image.get_rect()
                    break

        self.x = 0
        self.y = 0
        DEBUG(" Exit>>")

    def set_play_rect(self, rect):
        self.play_rect = rect

    def handle_input(self):
        DEBUG("<< Enter")
        keys = pg.key.get_pressed()
        if keys:
            if keys[pg.K_UP] or keys[pg.K_w]:
                INFO("key up pressed!! ")
                self.y -= 5
                if self.play_rect:
                    if self.y < self.play_rect.y:
                        self.y = self.play_rect.y

            if keys[pg.K_DOWN] or keys[pg.K_s]:
                INFO("key down pressed!! ")
                self.y += 5
                if self.play_rect:
                    if self.y + self.rect.height/2 > self.play_rect.y + self.play_rect.height:
                        self.y = -self.rect.height/2 + self.play_rect.y + self.play_rect.height

            if keys[pg.K_LEFT] or keys[pg.K_a]:
                INFO("key left pressed!! ")
                self.x -= 5
                if self.play_rect:
                    if self.x < self.play_rect.x:
                        self.x = self.play_rect.x

            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                INFO("key right pressed!! ")
                self.x += 5
                if self.play_rect:
                    if self.x  > self.play_rect.x + self.play_rect.width:
                        self.x = self.play_rect.x + self.play_rect.width

                    #if self.x + self.rect.width > self.play_rect.x + self.play_rect.width:
                    #    self.x = -self.rect.width + self.play_rect.x + self.play_rect.width

            if keys[pg.K_z] or keys[pg.K_PERIOD]:
                INFO("key [Fire] pressed!! ")
                ## Fire
                # sound effect
                # bullet object create
            if keys[pg.K_x] or keys[pg.K_SLASH]:
                INFO("key [Misile] pressed!! ")
                ## Fire
                # sound effect
                # Misile object create
            #else:
            #    INFO(f"key [{keys}] pressed!! ")
        #keys = pg.key.get_pressed()
        #if self.rect.collidepoint(pg.mouse.get_pos()):
        #    if pg.mouse.get_pressed() == (1, 0, 0):
        #        INFO("Mouse Button pressed!! ")
        #        self.change_text("마우스 눌렀어.")
        #    if keys[pg.K_SPACE]:
        #        INFO("Space key pressed!! ")
        DEBUG(" Exit>>")

    def move_xy(self, x, y):
        DEBUG("<< Enter")
        self.x = x
        self.y = y
        DEBUG(" Exit>>")

    def apply_position(self):
        DEBUG("<< Enter")
        self.rect.centerx, self.rect.centery = self.x, self.y
        DEBUG(" Exit>>")

    def animation(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def update(self):
        DEBUG("<< Enter")
        self.dirty = 1
        self.handle_input()
        self.apply_position()
        self.animation()
        DEBUG(" Exit>>")

class ShootingScene(Scene):
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

    def start(self):
        DEBUG("<< Enter")
        DEBUG(">>>>>>>>>>>>>>>> [%s] Scene START >>>>>>>>>>>>>>>>"%(self.name))
#        self.board = Board(219, 41, 585, 407, DARKOLIVEGREEN)
#        self.menu_title = Label("메뉴를 선택해 주세요.", (348, 63))
#        self.exit_button = Button("종 료", (447, 348), WHITE)
#        self.play_button = Button("PLAY", (447, 227), WHITE)
        # 정렬
#        self.menu_title.rect.centerx = self.board.rect.centerx
#        self.exit_button.rect.centerx = self.board.rect.centerx
#        self.menu_title.rect.centerx = self.board.rect.centerx
#        self.board.add(self.allObjGroup)
#        self.menu_title.add(self.allObjGroup)
#        self.exit_button.add(self.allObjGroup)
#        self.play_button.add(self.allObjGroup)
        #self.allObjGroup.add(self.board)
        #self.allObjGroup.add(self.menu_title)
        #self.allObjGroup.add(self.exit_button)
        #self.allObjGroup.add(self.play_button)

#        self.exit_button.setOnClick(lambda stage="", onGoing=False : self.gotoStage(stage, onGoing))
#        self.play_button.setOnClick(lambda stage="Stage1", onGoing=False : self.gotoStage(stage, onGoing))
        

        #Background 로딩
        self.bg = StaticBackground("space", PLAY_AREA)

        playground_width  = PLAY_AREA[0]
        playground_height = PLAY_AREA[1]

        pad_rect = self.gamepad.get_rect()

        playground_x = int((pad_rect.width  - playground_width ) / 2)
        playground_y = int((pad_rect.height - playground_height) / 2)

        self.play_rect = pg.Rect(playground_x, playground_y, playground_width, playground_height)
        INFO(f"**playground_x = [{playground_x}]")
        INFO(f"**playground_y = [{playground_y}]")
        INFO(f"**playground_width  = [{playground_width}]")
        INFO(f"**playground_height = [{playground_height}]")
        INFO(f"**self.play_rect = [{self.play_rect}]")

        #게임 객체 로딩
        #air_craft = AirScraft("spaceship", (PLAY_AREA[1]/8, PLAY_AREA[0]/8))
        air_craft = AirScraft("spaceship", (playground_height/8, playground_width/8))
        air_craft.set_play_rect(self.play_rect)
        air_craft.move_xy(self.play_rect.centerx, self.play_rect.bottom - 50)

        self.player = pg.sprite.GroupSingle()
        air_craft.add(self.player)

        #그룹분리
        ## 전체 그룹에 추가
        self.allObjGroup = pg.sprite.Group()

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
                            #self.drag_object.handle_input()
 
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
            pygame.draw.line(self.gamepad, RED, (self.play_rect.x, self.play_rect.y) , (self.play_rect.x + self.play_rect.width, self.play_rect.y), 4)
            #pygame.draw.rect(self.gamepad, RED, self.play_rect)
            # 객체 이벤트 처리
            # 객체 그리기
            self.allObjGroup.draw(self.gamepad)
            self.allObjGroup.update()

            self.player.draw(self.gamepad)
            self.player.update()


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
    menuScene = ShootingScene("menu", gamepad)
    menuScene.start()
    pg.quit()