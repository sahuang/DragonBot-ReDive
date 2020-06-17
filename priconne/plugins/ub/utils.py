from os import path
from random import randrange

from priconne.plugins.ub.character_data import CHARACTER, find_char_by_name

async def get_ub_of_character(character: str) -> str:

    char_id = await find_char_by_name(character)
    
    if char_id == 1000:
        return f'不支持当前角色UB。建议使用/laopo'

    return f'[CQ:record,file=/pcr/{char_id}.mp3]'

async def get_ub_random() -> str:
    
    chara_count = len(CHARACTER)
    chara_list = list(CHARACTER.keys())
    char_id = chara_list[randrange(chara_count)]
    while char_id < 1000 or char_id > 1060:
        char_id = chara_list[randrange(chara_count)]

    return f'[CQ:record,file=/pcr/{char_id}.mp3]'

async def get_manual() -> str:

    return f'参数请使用国服称呼，目前支持至纯。'