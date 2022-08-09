from ursina import *

window.title = " The Clock"
window.borderless = False
base_temps = time.time()
reset_time = time.time()
window.size = (1200, 600)


def reset():
    global reset_time, score_time
    reset_time = time.time() - score_time
    print(reset_time)


def update():
    global text, reset_time, score_time
    score_time = time.time() - base_temps

    # Digital clock
    text.y = 1
    text = Text(f" {str(format(score_time, '.2f'))}",
                position=(0, .4), origin=(0, 0), scale=2, background=True)
    format(score_time, '.2f')


format(reset_time, '.2f')

# Main game
app = Ursina()
wall = Entity(model='quad', scale=(15, 10))

text = Text(text='')
clock = Entity(model='circle', color=color.black, scale=5)

b_pause = Button(x=-0, y=-0.07, scale=0.10, text='pause', color=color.azure, highlight_color= color.brown, text_origin=(-.5, 0))
b_pause.on_click = application.pause  # assign a function to the button.


b_resume = Button(x=0.25, y=-0.07, scale=(0.131, 0.040), icon="assets/quit.png")
b_resume.on_click = application.resume


b_reset = Button(x=0.50, y=-0.07, scale=0.10, text='reset', color=color.black, highlight_color= color.brown,  text_origin=(-0.25, 0))
b_reset.on_click = reset  # assign a function to the button.


app.run()
