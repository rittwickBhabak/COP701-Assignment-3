from io import BytesIO
from PIL import Image
import tkinter as tk
import threading 

def image_to_data(im):
    with BytesIO() as output:
        im.save(output, format="PNG")
        data = output.getvalue()
    return data

filename = '1ac.gif'    # https://cdn2.thecatapi.com/images/1ac.gif
n_frames = 2            # 52 but only 2 to show to difference

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()

# images1 = [tk.GoodPhotoImage(file=filename, format=f'gif -index {i}') for i in range(n_frames)]
images1 = [tk.PhotoImage(file=filename, format=f'gif -index {i}') for i in range(n_frames)]
for i in range(n_frames):
    label = tk.Label(frame1, image=images1[i])
    label.pack(side='left')

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

def test(labels):
    print('Creating images')
    for label in labels:
        label.pack(side='left')

thread = threading.Thread(target=test, args=(labels,))
thread.start()

root.mainloop()