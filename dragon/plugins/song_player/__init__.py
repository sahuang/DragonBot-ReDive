from nonebot import on_command, CommandSession, get_bot

from .utils import *

@on_command('song', aliases=('play', 'music', '音乐'), only_to_me=False)
async def player(session: CommandSession):

    clip = await get_clip()
    await session.send(clip)