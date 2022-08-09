from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina import time

window.title = " The Maze"
window.borderless = False
base_temps = time.time()

class Enemy(Entity):

    def __init__(self, x, y):
        super().__init__()
        self.model = 'cube'
        self.color = color.red
        self.x = x
        self.y = y
        self.collider = 'box'


def update():
    global text, enemy, speed
    score_time = time.time() - base_temps

    # Digital clock
    text.y = 1
    text = Text(f" {str(format(score_time, '.2f'))}",
                position=(0, .4), origin=(0, 0), scale=1, background=True)
    format(score_time, '.2f')

    for enemy in enemies:
        enemy.x += speed * time.dt
        if player.intersects(enemy).hit:
            print('die')
            player.color = color.azure
            player.position = player.start_position


def input(key):
    if key == 'space':
        _ = Audio('hit_jump.wav', pitch=1, autoplay=True)


enemies = []

enemy = Enemy(15, 35.5)
enemies.append(enemy)

enemy = Enemy(50, 35.5)
enemies.append(enemy)

enemy = Enemy(65, 35.5)
enemies.append(enemy)

app = Ursina()

speed = 1

player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)

ground = Entity(model='quad', scale_x=10, collider='box', color=color.black)

quad = load_model('quad', use_deepcopy=True)

level_parent = Entity(model=Mesh(vertices=[], uvs=[]), texture='white_cube')

Audio(sound_file_name='Retro_Platforming.mp3', autoplay=True, loop=True, auto_destroy=False)

hit_jump = Audio('hit_jump.wav', pitch=1, autoplay=True)


def make_level(texture):
    # destroy every child of the level parent.
    # This doesn't do anything the first time the level is generated, but if we want to update it several times
    # this will ensure it doesn't just create a bunch of overlapping entities.
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None

        for x in range(texture.width):
            col = texture.get_pixel(x, y)

            # If it's black, it's solid, so we'll place a tile there.
            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x + .5, y + .5, 0) for e in
                                                quad.generated_vertices]  # copy the quad model, but offset it with
                # Vec3(x+.5,y+.5,0)
                level_parent.model.uvs += quad.uvs
                # Entity(parent=level_parent, position=(x,y), model='cube', origin=(-.5,-.5), color=color.gray,
                # texture='white_cube', visible=True)
                if not collider:
                    collider = Entity(parent=level_parent, position=(x, y), model='quad', origin=(-.5, -.5),
                                      collider='box', visible=False)
                else:
                    # instead of creating a new collider per tile, stretch the previous collider right.
                    collider.scale_x += 1
            else:
                collider = None

            # If it's green, we'll place the player there. Store this in player.start_position so we can reset the
            # plater position later.
            if col == color.green:
                player.start_position = (x, y)
                player.position = player.start_position

            # if col == color.salmon:
            #    position_enemy = Entity(parent=level_parent, position=(x, y), model='sphere', origin=(-.5, -.5),
            #                            collider='box', visible=True, color=color.yellow)
            #    position_enemy.start_position = (x, y)

    level_parent.model.generate()


make_level(load_texture('platformer_tutorial_level'))  # generate the level

camera.orthographic = True
EditorCamera()

camera.position = (16 / 2, 8)
camera.fov = 16
camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))
player.traverse_target = level_parent

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')


player.start_position = player.position

button_2 = Button(x=-0.75, scale=0.05, color=rgb(250, 128, 114))
button_2.tooltip = Tooltip(f'<gold>The Maze\n<default>Find a way out.\n')
button_2.on_click = player.start_position


b_3 = Button(x=-0, y=-0.07, scale=0.10, text='pause', color=color.azure, text_origin=(-.5, 0))
b_3.on_click = application.pause  # assign a function to the button.
b_3.tooltip = Tooltip('exit')

b_4 = Button(x=0.25, y=-0.07, scale=0.10, text='resume', color=color.azure, text_origin=(-0.25, 0))
b_4.on_click = application.resume  # assign a function to the button.
b_4.tooltip = Tooltip('exit')

app.run()
