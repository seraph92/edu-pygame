
from BKLOG import *

class Scenes: 
    scenes = {}
    def __init__(self):
        DEBUG("<< Enter")
        DEBUG(" Exit>>")

    def addScene(self, name):
        DEBUG("<< Enter")
        self.scenes[name] = Scene(name)
        DEBUG(" Exit>>")

    def start(self, name):
        DEBUG("<< Enter")
        self.scenes[name].start()
        DEBUG(" Exit>>")

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
        DEBUG(">>>>>>>>>>>>>>>> Scene START >>>>>>>>>>>>>>>>")
        DEBUG(" Exit>>")