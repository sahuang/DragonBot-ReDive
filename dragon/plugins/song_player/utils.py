from os import listdir, path
from random import choice, randrange
from string import ascii_letters

from pydub import AudioSegment

BASE = '酷Q Pro\\data\\record\\music\\'

async def get_clip() -> str:

    AudioSegment.ffmpeg = "Desktop\\ffmpeg"

    while True:
        basedir = 'Desktop\\music\\'
        file = choice([x for x in listdir(basedir) if path.isfile(path.join(basedir, x))])
        print(file)
        if file.lower().endswith('.mp3'):
            # cut a 15-second clip
            sound = AudioSegment.from_mp3(basedir + file)
            start = randrange(len(sound) - 15000)
            clip = sound[start:start + 15001]
            rand_name = ''.join(choice(ascii_letters) for i in range(10)) + '.mp3'
            clip.export(BASE + rand_name, format="mp3")
            return f'[CQ:record,file=/music/{rand_name}]'