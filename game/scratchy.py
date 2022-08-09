from ursina import *

a = Audio(sound_file_name='Retro_Platforming.mp3', pitch=1, loop=True, autoplay=True)

a.volume=0

def input(key):
    if key == 'f':
        a.fade_out(duration=4, curve=curve.linear)

def update():
    print(a.time)