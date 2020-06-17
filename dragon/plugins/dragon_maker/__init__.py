from nonebot import on_command, CommandSession
from nonebot.permission import PRIVATE

from .utils import make_dragon

ERROR_MSG = "输入不合规。请重新输入。"

@on_command('dragonmaker', aliases=('造龙', '生成龙图'), only_to_me=False, permission=PRIVATE)
async def dragonmaker(session: CommandSession):

    # 从会话状态中获取需要龙化的图片，如果当前不存在，则询问用户
    base = session.get('base', prompt='请向机器人发送一张背景图片。')

    # 获取位置
    pos = session.get('pos', prompt='请输入龙在背景图中的位置x y，用空格分隔。以左上角为原点，' + \
        'x和y代表在背景图中长和宽的位置比，范围是[0, 1]。例如0 0代表左上， 0.5 0.5代表中心。')

    # 获取龙图大小
    size = session.get('size', prompt='请输入龙的相对大小，即龙图长与背景图长的比值，范围是(0, 1]。')

    # 向用户发送生成的龙图
    dragon = await make_dragon(base, pos, size)
    await session.send(dragon)

@dragonmaker.args_parser
async def _(session: CommandSession):
    arg = session.current_arg

    if session.current_key == 'base':
        if 'CQ:image' in arg and 'gif' not in arg:
            session.state['base'] = session.current_arg_images[0]
        else:
            session.pause('请发送一张图片。(暂不支持gif)')

    if session.current_key == 'pos':
        # x y
        pos_list = session.current_arg_text.split(" ")
        if len(pos_list) != 2:
            session.pause(ERROR_MSG)
        try:
            x = float(pos_list[0])
            y = float(pos_list[1])
        except ValueError:
            session.pause(ERROR_MSG)

        if (x < 0 or x > 1 or y < 0 or y > 1):
            session.pause(ERROR_MSG)

        session.state['pos'] = {'width': x, 'height': y}
    
    if session.current_key == 'size':
        size = session.current_arg_text.strip()
        try:
            x = float(size)
        except ValueError:
            session.pause(ERROR_MSG)

        if x <= 0 or x > 1:
            session.pause(ERROR_MSG)

        session.state['size'] = x