from os import path

import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'priconne', 'plugins'),
        'priconne.plugins'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'dragon', 'plugins'),
        'dragon.plugins'
    )
    nonebot.run()