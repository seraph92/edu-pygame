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
    __backObjList = []
    __image_name = ""
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self):
        DEBUG("<< Enter")
        DEBUG('BG_IMG_FILE["background"] = [%s]'% BG_IMG_FILE["background"])
        self.__image_name = BG_IMG_FILE["background"]
        self.__backObjList.append(pg.image.load(IMG_PATH + '/' + BG_IMG_FILE["background"]))
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
    __background = []

    def __init__(self):
        DEBUG("<< Enter")
        self.__background.append(BackgroundImage())
        self.__background.append(copy.deepcopy(self.__background[0]))
        DEBUG(" Exit>>")

    def getBackground(self, index: int) -> BackgroundImage:
        DEBUG("index=[%s]"%index)
        return self.__background[index]

    def getBackgrounds(self) -> [BackgroundImage]:
        return self.__background

    def status(self) -> str:
        rt_str = ""
        for index, background in enumerate(self.__background):
            rt_str += background.status() + "\n"

        return rt_str



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
        first_back = self.getBackground(0)
        second_back = self.getBackground(1)
        second_back.setPosition(first_back.width, 0)
        DEBUG(" Exit>>")

    def status(self):
        return "speed = [%d], refresh_rate=[%d], tick=[%d]"%(self.__speed, self.__rr, self.__tick) + "\n" + super().status()

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
