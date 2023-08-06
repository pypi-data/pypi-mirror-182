import math

from PyGine import Debug, PyGinegame as Game

from PyGine.Camera import Camera
from PyGine.ColliderComponent import ColliderComponent
from PyGine.Component import Component
import pygame as pg
class CircleColliderComponent(ColliderComponent) :

    def update(self,dt) :
        if(Debug.Debug.ShowCollidersBox) :
            pg.draw.circle(Game.get().surface,(0,0,0,100),(int(self.transform.position.x - (Camera.PX+Camera.DX)),
                         int(self.transform.position.y - (Camera.PY+Camera.DY)) ) , self.transform.scale.x*Camera.ZX,1)

    def CallCollide(self,o):
        self.parent.onCollision(o)

    def collide(self,o):
        closestX = o.transform.position.x
        closestY = o.transform.position.y
        if abs(self.transform.position.x - (o.transform.position.x+o.transform.scale.x)) < abs(self.transform.position.x - closestX) :
            closestX = o.transform.position.x+o.transform.scale.x
        if abs(self.transform.position.y - (o.transform.position.y+o.transform.scale.y)) < abs(self.transform.position.y - closestY) :
            closestY = o.transform.position.y+o.transform.scale.y
        if math.sqrt((self.transform.position.x-closestX)**2 + (closestY-self.transform.position.y)**2) < self.transform.scale.x :
            #call collision
            self.CallCollide(o)
        return