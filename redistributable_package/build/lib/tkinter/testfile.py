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

class PointFromList(Point):
    def __init__(self, height, width, data):
        super().__init__(height, width)
        domain = list(map(lambda x: x[0], data))    
        co_domain = list(map(lambda x: x[1], data))
        self.domain = self.get_scaled_values(domain, width)
        self.co_domain = self.get_scaled_values(co_domain, height)
        self.set_points(self.domain, self.co_domain)

class PointFromFunction(Point):
    def __init__(self, height, width, eval=None, domain=[]):
        super().__init__(height, width, eval, domain)
        self.prepare_field()
        self.set_points(self.domain, self.co_domain)

    def prepare_field(self):
        x = self.expand_domain(self.domain)
        result = self.get_y_values(self.eval, x)
        
        self.domain = list(map(lambda x: x[0], result))
        self.co_domain = list(map(lambda x: x[1], result))
        self.domain = self.get_scaled_values(self.domain, self.width)
        self.co_domain = self.get_scaled_values(self.co_domain, self.height)

    def get_y_values(self, eval, x):
        result = []
        for i in x:
            try:
                result.append((i, eval(i)))
            except:
                pass 
        return result

    def expand_domain(self, domain):
        x = [] 
        low = domain[0]
        high = domain[1] 
        diff = 0.01
        while low<=high:
            x.append(low)
            low = low + diff 
        return x 




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
        if ty=='func':
            points = PointFromFunction(self.height, self.width, eval=fn, domain=domain)
        elif ty=='scatter':
            points = PointFromList(self.height, self.width, data)

        for x_, y_ in points.points:
            x0 = x_-self.daig
            y0 = y_-self.daig
            x1 = x_+self.daig
            y1 = y_+self.daig
            self.canvas.create_oval(x0, y0, x1, y1)
            self.canvas.update()


