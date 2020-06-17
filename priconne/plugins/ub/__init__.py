from nonebot import on_command, CommandSession, get_bot

from .utils import *

@on_command('pcr', aliases=('PCR', '公主'), only_to_me=False)
async def ub(session: CommandSession):

    character = session.get('character')
    if character in ["r", "rand", "random", "随机"]:
        random_ub = await get_ub_random()
        await session.send(random_ub)
    elif character in ["help", "h", "帮助"]:
        helper = await get_manual()
        await session.send(helper)
    else:
        character_ub = await get_ub_of_character(character)
        await session.send(character_ub)

@ub.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['character'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请重新输入...')

    session.state[session.current_key] = stripped_arg