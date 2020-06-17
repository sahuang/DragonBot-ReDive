from os import listdir, path
from random import randrange, choice

from priconne.plugins.ub.character_data import CHARACTER, find_char_by_name

basedir = '酷Q Pro\\data\\record\\common'

async def get_waifu_voice(character: str) -> str:

    char_id = await find_char_by_name(character)
    
    if char_id == 1000:
        return f'角色不存在或不支持当前角色日常配音。'

    # get random mp3 starting with character
    new_dir = path.join(basedir, str(char_id))

    file = choice([x for x in listdir(new_dir) if path.isfile(path.join(new_dir, x))])

    return f'[CQ:record,file=/common/{str(char_id)}/{file}]'

async def get_waifu_random() -> str:

    chara_list = list(CHARACTER.keys())
    char_id = chara_list[randrange(len(CHARACTER))]
    new_dir = path.join(basedir, str(char_id))

    file = choice([x for x in listdir(new_dir) if path.isfile(path.join(new_dir, x))])

    return f'[CQ:record,file=/common/{str(char_id)}/{file}]'