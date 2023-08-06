
import pygame as pg
from PyGine.ColliderComponent import ColliderComponent

import PyGine
from PyGine.Camera import Camera

import PyGine.PyGinegame as Game

from PyGine import Debug



class BoxColliderComponent(ColliderComponent) :
    def __init__(self,parent) :
        super().__init__(parent)
        self.parent = parent
        self.transform = parent.transform

    def update(self,dt) :
        if (Debug.Debug.ShowCollidersBox):
            pg.draw.rect(Game.get().surface, (0,0,0),((
                                                 int(self.transform.position.x - (Camera.PX+Camera.DX)),
                                                 int(self.transform.position.y - (Camera.PY+Camera.DY)) ),
                                                 (int(self.transform.scale.x * Camera.ZX),
                                                  int(self.transform.scale.y * Camera.ZY))),1)

    def CallCollide(self,o):
        self.parent.onCollision(o)
    def collide(self,o):

        if (o.transform.position.x+o.transform.scale.x > self.transform.position.x > o.transform.position.x ) or \
                (self.transform.position.x+self.transform.scale.x > o.transform.position.x > self.transform.position.x ):
            if (o.transform.position.y + o.transform.scale.y > self.transform.position.y > o.transform.position.y) or \
                    (self.transform.position.y + self.transform.scale.y > o.transform.position.y > self.transform.position.y):
                return self.CallCollide(o)
        return
