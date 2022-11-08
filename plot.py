from tkinter import * 
from tkinter.graphplotter import Plot
import math 
import random 

def gen(n=100, high=100, low=-100):
    x = random.randint(low, high)
    y = random.randint(low, high)
    return [(x, y) for _ in range(n) ]


def sq(x):
    return x

root = Tk() 
root.geometry('500x600')

plot = Plot(root, height=200, width=300, bg='white')
plot.draw(arg={'fn':sq, 'domain':[0, 100], 'type':'func'})
plot.pack()

root.mainloop()