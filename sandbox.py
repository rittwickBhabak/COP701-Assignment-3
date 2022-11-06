import tkinter as tk
import os 

root = tk.Tk()

frame = tk.Frame()
frame.pack()
gif_image = tk.GifImage(os.path.join(os.getcwd(), '1ac.gif'), frame)
gif_image.show()

root.mainloop()