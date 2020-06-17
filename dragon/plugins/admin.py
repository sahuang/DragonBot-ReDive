from nonebot import on_request, RequestSession, get_bot, CommandSession
from aiocqhttp import Event, CQHttp

bot = get_bot()

@on_request('group')
async def _(session: RequestSession):
    await session.approve()

@on_request('friend')
async def _(session: RequestSession):
    await session.approve()

@bot.on_message('private')
async def _(event: Event):
    await bot.send_private_msg(user_id=441579849, message=event.message)