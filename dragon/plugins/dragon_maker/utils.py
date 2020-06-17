from os import listdir, path
from random import choice, randint
from string import ascii_letters

from PIL import Image
import PIL
import requests
import io

BASE_DIR = '酷Q Pro\\data\\image'

async def make_dragon(base: str, pos: dict, size: float) -> str:
    '''
    输入合法图片，龙图期望位置以及大小，返回加工后图片。
    龙图随机提供，resize到目标大小再paste进背景图片。

    :param str base: Image URL
    :param dict pos: Dictionary of width and height of relative position for dragon image
    :param float size: Relative size of dragon compared to background image
    :return: Modified image path
    '''

    # get base image
    response = requests.get(base)
    base_img = Image.open(io.BytesIO(response.content), 'r')

    # get random dragon image
    dragon_dir = BASE_DIR + '\\dragon_thumbnail\\'
    rand_choice = choice([x for x in listdir(dragon_dir) if path.isfile(path.join(dragon_dir, x))])
    dragon_image = Image.open(dragon_dir + rand_choice, 'r')

    # process images
    img_w, img_h = base_img.size
    background = Image.new('RGB', (img_w, img_h), (255, 255, 255))
    background.paste(base_img, (0, 0))

    dragon_image = dragon_image.resize((int(img_w * size), int(img_w * size)))
    dra_w, dra_h = dragon_image.size
    top_left_width = max(int(pos['width'] * img_w - dra_w // 2), 0)
    top_left_height = max(int(pos['height'] * img_h - dra_h // 2), 0)

    # IMPORTANT: change color of dragon's area to white first before pasting
    # Process every pixel
    for x in range(top_left_width + 7, top_left_width + dra_w - 7):
        for y in range(top_left_height + 5, top_left_height + dra_h - 5):
            background.putpixel((x,y), (randint(230, 255), randint(230, 255), randint(230, 255)))

    offset = (top_left_width, top_left_height)
    background.paste(dragon_image, offset, mask=dragon_image)

    # save image
    save_dir = BASE_DIR + '\\generated_dragon\\'
    rand_name = ''.join(choice(ascii_letters) for i in range(10)) + '.png'
    background.save(save_dir + rand_name)

    return f'[CQ:image,file=/generated_dragon/{rand_name}]'