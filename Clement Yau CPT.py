import arcade


WIDTH = 640
HEIGHT = 480

# start player position in middle of window
player_x = 10
player_y = HEIGHT/2

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


def on_update(delta_time):
    global up_pressed, down_pressed, player_y
    if up_pressed:
        player_y += 5

    elif down_pressed:
        player_y -= 5

    if player_x < player_x // 2 or player_x > WIDTH - player_x // 2:
        delta_y == 0

    if player_y < player_y // 2 or player_y > HEIGHT - player_y // 2:
        delta_y == 0


def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_filled(player_x, player_y, 10, 60, arcade.color.BLUSH)

def on_key_press(key, modifiers):
    global up_pressed, down_pressed
    if key == arcade.key.W:
        up_pressed = True

    elif key == arcade.key.S:
        down_pressed = True


def on_key_release(key, modifiers):
    global up_pressed, down_pressed
    if key == arcade.key.W:
        up_pressed = False

    elif key == arcade.key.S:
        down_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
