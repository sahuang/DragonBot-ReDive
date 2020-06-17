from os import listdir, path
from random import choice

async def get_dragon() -> str:

    basedir = '酷Q Pro\\data\\image\\dragon'
    file = choice([x for x in listdir(basedir) if path.isfile(path.join(basedir, x))])

    return f'[CQ:image,file=/dragon/{file}]'