from nonebot import on_command, CommandSession

@on_command('help', aliases=('h', '帮助'), only_to_me=False)
async def manual(session: CommandSession):

    await session.send(f'[CQ:image,file=/admin/manual.png]')

@manual.args_parser
async def _(session: CommandSession):
    # do nothing
    return