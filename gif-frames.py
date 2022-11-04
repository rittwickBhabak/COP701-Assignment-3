from PIL import Image

num_key_frames = 8

with Image.open('1ac.gif') as im:
    print(im)
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        # im.save('imgs/{}.png'.format(i))