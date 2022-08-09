from ursina import *

window.title = " The Clock"
window.borderless = False


def reset():
    global reset_time, score_time
    reset_time = time.time() - time.time()
    print(reset_time)


# def resume():
#    global reset_time, score_time
#    resume_time = time.time() - base_temps - score_time
#    print(resume_time)


def update():
    global text

    # Digital clock
    text.y = 1
    text = Text(f" {str(format(reset_time, '.2f'))}",  # modif score_time / reset
                position=(0, .4), origin=(0, 0), scale=2, background=True)
    format(score_time, '.2f')


# Main game
app = Ursina()
wall = Entity(model='quad', scale=(15, 10))

text = Text(text='')
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
