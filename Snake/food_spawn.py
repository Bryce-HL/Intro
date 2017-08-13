from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from random import randint

class MyApp (ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

    
    
    def spawn_food(self):       
        self.foodActor = Actor("models/box")
        self.foodActor.setScale(0.005, 0.005, 0.005)
        self.foodActor.reparentTo(self.render)
        self.foodActor.loop()

app = MyApp()
app.run()

