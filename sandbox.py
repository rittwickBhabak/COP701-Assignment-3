import tkinter as tk
import os 

root = tk.Tk()

gif_image = tk.GifImage(root, os.path.join(os.getcwd(), '1ac.gif'), relief=tk.GROOVE, borderwidth=10, pady=20, padx=30, width=100, height=100, bg='yellow')
gif_image.show()
gif_image.pack()

def on_closing():
    gif_image.stop_threads = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def click():
    print('I am clicked')

button = tk.Button(text='This is a text', command=click)
button.pack()

root.mainloop()