from ursina import *

window.title = " The Clock"
window.borderless = False


class TimerError(Exception):

    """A custom exception used to report errors in use of Timer class"""


class Timer:

    def __init__(self):

        self._start_time = None


    def start(self):

        """Start a new timer"""

      # if self._start_time is not None:

      #     raise TimerError(f"Timer is running. Use .stop() to stop it")


        self._start_time = time.perf_counter()


    def stop(self):

        """Stop the timer, and report the elapsed time"""

        if self._start_time is None:

            raise TimerError(f"Timer is not running. Use .start() to start it")


        elapsed_time = time.perf_counter() - self._start_time

        self._start_time = None

        print(f"Elapsed time: {elapsed_time:0.2f} seconds")


t = Timer()
t.start()


def update():
    global text

    # Digital clock
    text.y = 1
    text = Text(f" {(format(time.perf_counter(), '.2f'))}",
                position=(0, .4), origin=(0, 0), scale=2, background=True)



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
b_reset.on_click = t.stop() # assign a function to the button.

app.run()
