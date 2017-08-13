from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, LPoint3
from random import randint

SPRITE_POS = 55 

class MyApp (ShowBase):

    def loadObject(tex=None, pos=LPoint3(0, 0), depth=SPRITE_POS, scale=1,
               transparency=True):

               self.food = loadObject("square.jpg")

    def __init__(self):
        ShowBase.__init__(self)

    
        self.setBackgroundColor((0, 0, 1, 2))

        
        
    
    def spawn_food(self):       
        self.foodActor = Actor("models/box")
        self.foodActor.setScale(0.005, 0.005, 0.005)
        self.foodActor.reparentTo(self.render)
        self.foodActor.loop()

app = MyApp()
app.run()

