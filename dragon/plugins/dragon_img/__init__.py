from nonebot import on_command, CommandSession, get_bot

from .utils import get_dragon

@on_command('dragon', aliases=('龙图', '龙'), only_to_me=False)
async def dragonimg(session: CommandSession):

    dragon = await get_dragon()
    await session.send(dragon)

@dragonimg.args_parser
async def _(session: CommandSession):
    # do nothing
    return