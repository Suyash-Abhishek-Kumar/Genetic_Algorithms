from random import random
from math import sqrt, atan2, degrees

def stabilize(num, old_start, old_end, new_start, new_end):
        if old_end == 0: old_end = 1
        old_range = old_end - old_start
        new_range = new_end - new_start
        return ((num - old_start) * new_range / old_range) + new_start

def randomV():
    return Vector2D([stabilize(round(random(), 4), 0,1,-1,1), stabilize(round(random(), 4), 0,1,-1,1)])

class Vector2D:
    def __init__(self, coords = None):
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0]
        self.magnitude = sqrt(self.coords[0]**2 + self.coords[1]**2)
    
    def _update_magnitude(self):
        self.magnitude = sqrt(self.coords[0]**2 + self.coords[1]**2)
    
    def add(self, other):
        if type(other) == Vector2D:
            self.coords[0] += other.x()
            self.coords[1] += other.y()
        elif type(other) == tuple:
            self.coords[0] += other[0]
            self.coords[1] += other[1]
    
    def mul(self, other):
        self.coords[0] *= other
        self.coords[1] *= other
    
    def setMag(self, newMag):
        scaling_factor = newMag/self.magnitude
        self.coords[0] *= scaling_factor
        self.coords[1] *= scaling_factor
        self._update_magnitude()
    
    def heading(self):
        return degrees(atan2(self.coords[0], self.coords[1]))
    
    def limit(self, max_value):
        if self.magnitude > max_value:
            self.setMag(max_value)
    
    def dist(self, other):
        if type(other) == Vector2D:
            dist = ((self.coords[0] - other.x())**2 + (self.coords[1] - other.y())**2)**0.5
        elif type(other) == tuple:
            dist = ((self.coords[0] - other[0])**2 + (self.coords[1] - other[1])**2)**0.5
        return dist 

    def get(self): return self.coords
    def x(self): return self.coords[0]
    def y(self): return self.coords[1]