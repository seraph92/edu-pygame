import pygame as pg
from setting  import *
from Background import *
from BKLOG import *

class Scenes: 
    def __init__(self):
        DEBUG("<< Enter")
        self.scenes = {}
        #self.gamepad = gamepad
        DEBUG(" Exit>>")

    def addScene(self, name, scene):
        DEBUG("<< Enter")
        self.scenes[name] = scene
        DEBUG(" Exit>>")

    def start(self, name):
        DEBUG("<< Enter")
        scene = self.scenes[name]
        DEBUG(" scene start = [%s]"%scene.status())
        nextScene = scene.start()
        DEBUG(" Exit>>")
        return nextScene

    def status(self):
        str = ""
        for key, scene in self.scenes.items():
            DEBUG("key=[%s]"%(key))
            DEBUG("value=[%s]"%(self.scenes[key].name))
            str += "SCENE[%s]=[%s]\n"%(key, self.scenes[key].name)
        return str

class Scene:
    def __init__(self, name):
        DEBUG("<< Enter")
        self.name = name
        DEBUG(" Exit>>")

    def start(self):
        DEBUG("<< Enter")
        DEBUG(">>>>>>>>>>>>>>>> [%s] Scene START >>>>>>>>>>>>>>>>"%(self.name))
        DEBUG(" Exit>>")

    def status(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")
        return " Scene Name = [%s]"%(self.name)
