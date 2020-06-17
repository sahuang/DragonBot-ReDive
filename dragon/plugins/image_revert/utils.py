from os import listdir, path, stat
from random import choice, randint
from string import ascii_letters
import sys
import time
import math

from PIL import Image, ImageSequence
import PIL
import requests
import io

BASE_DIR = '酷Q Pro\\data\\image'

async def reverse_image(base: str) -> str:

    # get base image
    response = requests.get(base)
    im = Image.open(io.BytesIO(response.content))

    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    frames.reverse()

    # save image
    save_dir = BASE_DIR + '\\gifs\\'
    rand_name = ''.join(choice(ascii_letters) for i in range(10)) + '.gif'
    frames[0].save(save_dir + rand_name, save_all=True, append_images=frames[1:], transparency=255, disposal=2)

    tot_size = stat(save_dir + rand_name).st_size // 1024
    if tot_size > 1500:
        # needs resize to < 1.5MB
        resize_factor = math.sqrt(tot_size / 1500.)

        size = int(frames[0].size[0] / resize_factor), int(frames[0].size[1] / resize_factor)

        # Wrap on-the-fly thumbnail generator
        def thumbnails(frames):
            for frame in frames:
                thumbnail = frame.copy()
                thumbnail.thumbnail(size)
                yield thumbnail

        frames = thumbnails(frames)
        # Save output
        rand_name = ''.join(choice(ascii_letters) for i in range(10)) + '.gif'
        om = next(frames) # Handle first frame separately
        om.info = im.info # Copy sequence info
        duration_new = 0
        om.save(save_dir + rand_name, save_all=True, append_images=list(frames), transparency=255, disposal=2)
        return f'[CQ:image,file=/gifs/{rand_name}]'
    else:
        # all good
        return f'[CQ:image,file=/gifs/{rand_name}]'