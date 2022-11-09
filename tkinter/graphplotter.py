from tkinter import *
from tkinter import _cnfmerge 


class Point():
    """Generate list of points that will be plotted.

    This class will scale up/down the points to be ploted on the 
    screen such that all of the points withing the range must be 
    fitted into the rectangle of specified width and height.
    """

    def __init__(self, height, width, eval=None, domain=None):
        """Constructor of the Point class.

        Args:
            height (int): Height of the rectangle
            width (int): Width of the rectangle
            eval (fucntion, optional): The function using which the points will be plotted. Defaults to None.
            domain (list, optional): Domain of the function. Defaults to None.
        """
        
        self.height = height 
        self.width = width 
        self.eval = eval 
        self.domain = domain

    def set_points(self, domain, co_domain):
        """Generate the points and associate them to the class.

        Generates list of points of the form (x, y) which will
        be drawn on the canvas.

        Args:
            domain (list): list of integers
            co_domain (list): list of integers
        """

        self.result = zip(domain, co_domain)
        self.points = []
        for _, (x, y) in enumerate(self.result):
            self.points.append((x, self.height - y))

    def get_scaled_values(self, l, max_value):
        """Apply scaling to all of the points (x, y) such that 
        the fit into the specified rectangel of the specified height
        and width.

        Args:
            l (list): list of integers
            max_value (int): The maximum value of the list l

        Returns:
            list: list of integers after applying scaling 
        """

        try:
            scale = max_value / (max(l) - min(l))
        except:
            scale = 1
        shift = min(l)
        return list(map(lambda x: (x-shift)*scale, l))


class PointFromList(Point):
    """Generate points from a given list of points.

    Basically scale the list of points such that all of them fits 
    into the rectangle of specified width and height. This class
    is inherited from Point class. So for more details view
    the Point class.

    """

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


