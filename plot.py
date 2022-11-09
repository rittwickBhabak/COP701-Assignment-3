from tkinter import * 
from tkinter.graphplotter import Plot
import math 
import random 

def gen(n=100, high=100, low=-100):
    x = random.randint(low, high)
    y = random.randint(low, high)
    return [(random.randint(low, high), random.randint(low, high)) for _ in range(n) ]


def sq(x):
    return x + math.sin(x) 

root = Tk() 
root.geometry('500x600')

plot = Plot(root, height=200, width=300, bg='white')
plot.draw(arg={'type':'scatter', 'data':gen()})
# plot.draw(arg={'fn':sq, 'domain':[-6, 6], 'type':'func'})
plot.pack()

root.mainloop()