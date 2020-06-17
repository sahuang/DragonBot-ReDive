from nonebot import on_command, CommandSession, get_bot

from .utils import reverse_image

@on_command('reverse', aliases=('倒放', '倒'), only_to_me=False)
async def reverse(session: CommandSession):

    # 从会话状态中获取图片
    base = session.get('base', prompt='请向机器人发送gif。')

    # 向用户发送图
    reverted = await reverse_image(base)
    await session.send(reverted)

@reverse.args_parser
async def _(session: CommandSession):
    arg = session.current_arg

    if session.is_first_run:
        # 该命令第一次运行arg
        if 'CQ:image' in arg and 'gif' in arg:
            session.state['base'] = session.current_arg_images[0]
        return

    if session.current_key == 'base':
        if 'CQ:image' in arg and 'gif' in arg:
            session.state['base'] = session.current_arg_images[0]
        else:
            session.finish('请发送gif。')