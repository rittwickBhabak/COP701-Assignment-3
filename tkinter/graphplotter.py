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







class Plot(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf, **kw)
        cnf = _cnfmerge((cnf, kw))
        self.height=cnf.get('height')
        self.width=cnf.get('width')
        self.canvas = Canvas(self, height=self.height, width=self.width,  borderwidth=3, relief=GROOVE)
        self.daig = 0.0011
        self.canvas.pack()

    def draw(self, arg):
        domain = arg.get('domain', None)
        fn = arg.get('fn', None)
        ty = arg.get('type')
        data = arg.get('data', None)
        # print(height, width, domain)
        if ty=='scatter':
            points = PointFromList(self.height, self.width, data)

        for x_, y_ in points.points:
            x0 = x_-self.daig
            y0 = y_-self.daig
            x1 = x_+self.daig
            y1 = y_+self.daig
            self.canvas.create_oval(x0, y0, x1, y1)
            self.canvas.update()


