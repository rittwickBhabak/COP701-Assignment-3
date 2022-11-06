import tkinter as tk
import os 

root = tk.Tk()

frame = tk.Frame()
frame.pack()
gif_image = tk.GifImage(root, os.path.join(os.getcwd(), '1ac.gif'))
gif_image.show()

def click():
    print('I am clicked')

button = tk.Button(text='This is a text', command=click)
button.pack()

root.mainloop()