from nonebot import on_command, CommandSession, get_bot

from .utils import *

@on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=False)
async def waifu(session: CommandSession):

    character = session.get('character')

    if character in ["r", "rand", "random", "随机"]:
        random_waifu = await get_waifu_random()
        await session.send(random_waifu)
    else:
        waifu = await get_waifu_voice(character)
        await session.send(waifu)

@waifu.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['character'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请重新输入...')

    session.state[session.current_key] = stripped_arg