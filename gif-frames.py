from PIL import Image

num_key_frames = 8
with Image.open('1ac.gif') as im:
    # print(im.n_frames) 
    # print(im)
    for i in range(im.n_frames):
        im.seek(i)
        im.save('imgs/{}.png'.format(i))

