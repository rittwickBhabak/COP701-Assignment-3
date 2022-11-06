from io import BytesIO
from PIL import Image
import tkinter as tk
import threading 
import time

def image_to_data(im):
    with BytesIO() as output:
        im.save(output, format="PNG")
        data = output.getvalue()
    return data

filename = '1ac.gif'    # https://cdn2.thecatapi.com/images/1ac.gif
n_frames = 52            

root = tk.Tk()

im = Image.open(filename)

frame2 = tk.Frame(root)
frame2.pack()

images2 = []
labels = []
for i in range(n_frames):
    im.seek(i)
    images2.append(tk.PhotoImage(data=image_to_data(im)))
    labels.append(tk.Label(frame2, image=images2[i]))
    # label.pack(side='left')

def test(labels, frame):
    print('Creating images')
    frame_number = 0
    while True:
        labels[frame_number].pack(side='left')
        time.sleep(0.02)
        labels[frame_number].pack_forget()
        frame_number += 1
        frame_number = frame_number % 52


thread = threading.Thread(target=test, args=(labels,frame2))
thread.start()

def click():
    print('See, I am clicked.')

button = tk.Button(text='Click me', command=click)
button.pack()

root.mainloop()

