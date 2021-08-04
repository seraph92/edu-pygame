import pygame as pg
from setting  import *
import copy
#from typing import *

from BKLOG import *

class BackgroundImage:
    '''
    Background Image
    '''
    #__backObjList: List[pg.Surface] = []
    def __init__(self, imageId, resize=None):
        DEBUG("<< Enter")
        self.__backObjList = []
        self.__image_name = ""
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        DEBUG('BG_IMG_FILE[%s] = [%s]'% (imageId, BG_IMG_FILE[imageId]))
        self.__image_name = BG_IMG_FILE[imageId]
        tmp_img = pg.image.load(IMG_PATH + '/' + BG_IMG_FILE[imageId])
        if resize:
            self.image = pg.transform.scale( tmp_img, (resize[0], resize[1]) )
        else:
            self.image = tmp_img

        self.__backObjList.append(self.image)
        self.width  = self.__backObjList[0].get_width()
        self.height = self.__backObjList[0].get_height()
        DEBUG(" Exit>>")
    
    def getImageObj(self):
        return self.__backObjList[0]

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def moveLeft(self, offset):
        self.x -= offset
    
    def status(self):
        return "__image_name = [%s], x = [%d], y = [%d]" % (self.__image_name, self.x, self.y)


class Background:
    """
    Background
    """
    #__background: List[BackgroundImage]

    def __init__(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def status(self) -> str:
        DEBUG("<< Enter")
        DEBUG(" Exit>>")
        return ""

#class MenuBackground(Background):
class StaticBackground(Background):
    '''
    Static Background
    '''
 
    def __init__(self, imageId = "", resize=None):
        DEBUG("<< Enter")
        self.__background = []

        Background.__init__(self)
        bgImage = BackgroundImage(imageId, (resize[0], resize[1]))

        self.addBackgroundImage(bgImage)

        menu_back = self.getBackground(0)
        DEBUG(" Exit>>")

    def addBackgroundImage(self, image):
        DEBUG("<< Enter")
        self.__background.append(image)
        DEBUG(" Exit>>")

    def getBackground(self, index: int):
        DEBUG("index=[%s]"%index)
        return self.__background[index]

    def getBackgrounds(self):
        return self.__background


    def status(self):
        rt_str = ""
        for index, background in enumerate(self.__background):
            rt_str += background.status() + "\n"

        return rt_str

    def applyMove(self):
        DEBUG("<< Enter")
        DEBUG("Static Screen don't move!!")
        # move all background
        # check recycle background
        DEBUG(" Exit>>")

    def blit(self):
        DEBUG("<< Enter")
        for i, bg in enumerate(self.getBackgrounds()):
            DEBUG("back_obj = [%s]"%(bg.status()))
            back_obj = bg.getImageObj()

            obj_rect = back_obj.get_rect()
            pad_rect = self.gamepad.get_rect()

            blit_x = int((pad_rect.width  - obj_rect.width ) / 2)
            blit_y = int((pad_rect.height - obj_rect.height) / 2)

            #self.gamepad.blit(back_obj, (0, 0))
            self.gamepad.blit(back_obj, (blit_x, blit_y))
        DEBUG(" Exit>>")


    def update(self, gamepad):
        DEBUG("<< Enter")
        self.gamepad = gamepad
        self.applyMove()
        self.blit()
        DEBUG(" Exit>>")

class SlideLeftBackground(Background):
    '''
    Left sliding Background
    <<<<<====
    '''
    __speed = 120 # pixel per a second
    __rr = REFRESH_RATE # refresh rate per a second
    __tick = __speed / __rr

    def __init__(self):
        DEBUG("<< Enter")
        Background.__init__(self)
        self.__background = []
        bgImage = BackgroundImage("background")
        bgImage2 = BackgroundImage("background")
        self.addBackgroundImage(bgImage)
        self.addBackgroundImage(bgImage2)

        first_back = self.getBackground(0)
        second_back = self.getBackground(1)
        second_back.setPosition(first_back.width, 0)
        DEBUG(" Exit>>")

    def addBackgroundImage(self, image):
        DEBUG("<< Enter")
        self.__background.append(image)
        DEBUG(" Exit>>")

    def getBackground(self, index: int):
        DEBUG("index=[%s]"%index)
        return self.__background[index]

    def getBackgrounds(self):
        return self.__background

    def status(self):
        rt_str = ""
        for index, background in enumerate(self.__background):
            rt_str += background.status() + "\n"

        return "speed = [%d], refresh_rate=[%d], tick=[%d]"%(self.__speed, self.__rr, self.__tick) + "\n" + rt_str

    def applyMove(self):
        DEBUG("<< Enter")
        # move all background
        # check recycle background
        for i, bg in enumerate(self.getBackgrounds()):
            bg.moveLeft(self.__tick)
            # TO-DO :  [A]->[B]->[C] => [B]->[C]->[A] 가 될 수 있도록 수정 필요
            if bg.x + bg.width <= 0:
                bg.setPosition(bg.width, 0)
        DEBUG(" Exit>>")

    def blit(self):
        DEBUG("<< Enter")
        for i, bg in enumerate(self.getBackgrounds()):
            back_obj = bg.getImageObj()
            DEBUG("back_obj = [%s]"%(bg.status()))
            self.gamepad.blit(back_obj, (bg.x, bg.y))
        DEBUG(" Exit>>")

    def update(self, gamepad):
        DEBUG("<< Enter")
        self.gamepad = gamepad
        self.applyMove()
        self.blit()
        DEBUG(" Exit>>")

if __name__ == '__main__':
    pg.init()
    back = SlideLeftBackground()
    DEBUG("status : %s " % back.status())
    back.applyMove()
    DEBUG("status : %s " % back.status())
    pg.quit()
