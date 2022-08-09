import time

from ursina import *

window.title = " The Clock test"
window.borderless = False
base_temps = time.time()
reset_time = time.time()
score_time = time.time() - base_temps
is_paused = False


def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True


def reset():
    global reset_time, score_time
    reset_time = time.time() - score_time
    print(reset_time)


text = Text(text='')
text2 = Text(text='')
text3 = Text(text='')

text.y = 1

text = Text(f" {str(format(score_time, '.2f'))}",
             position=(1, .4), origin=(0, 0), scale=2, background=True)
format(score_time, '.2f')

while True:
    def update():
        global text, text2, text3, reset_time, score_time
        score_time = time.time() - base_temps

        # Digital clock
       #text.y = 1

       #text = Text(f" {str(format(score_time, '.2f'))}",
       #            position=(0, .4), origin=(0, 0), scale=2, background=True)
       #format(score_time, '.2f')



        text3.y = 1

        text3 = Text(f" {str(format(score_time, '.2f'))}",
                     position=(2, .4), origin=(0, 0), scale=2, background=True)
        format(score_time, '.2f')


    app = Ursina()
    wall = Entity(model='quad', scale=(15, 10))


    clock = Entity(model='circle', color=color.black, scale=5)

    b_pause = Button(x=-0, y=-0.07, scale=0.10, text='pause', color=color.azure, highlight_color=color.brown,
                     text_origin=(-.5, 0))
    b_pause.on_click = application.pause  # assign a function to the button.

    b_resume = Button(x=0.25, y=-0.07, scale=0.10, text='resume', color=color.azure, highlight_color=color.brown,
                      text_origin=(-0.25, 0))
    b_resume.on_click = application.resume

    b_reset = Button(x=0.50, y=-0.07, scale=0.10, text='reset', color=color.black, highlight_color=color.brown,
                     text_origin=(-0.25, 0))
    b_reset.on_click = reset  # assign a function to the button.

    app.run()
