from tkinter import *
from tkinter import _cnfmerge 


class Point():
    def __init__(self, height, width, eval=None, domain=None):
        self.height = height 
        self.width = width 
        self.eval = eval 
        self.domain = domain

    def set_points(self, domain, co_domain):
        self.result = zip(domain, co_domain)
        self.points = []
        for _, (x, y) in enumerate(self.result):
            self.points.append((x, self.height - y))

    def get_scaled_values(self, l, max_value):
        try:
            scale = max_value / (max(l) - min(l))
        except:
            scale = 1
        shift = min(l)
        return list(map(lambda x: (x-shift)*scale, l))










