import arcade


WIDTH = 1280
HEIGHT = 720

# player 1
player_1_x = 10
player_1_y = HEIGHT/2
# Variables to record if certain keys are being pressed.
player_1_up_pressed = False
player_1_down_pressed = False


# player 2
player_2_x = 1270
player_2_y = HEIGHT/2
# Variables to record if certain keys are being pressed.
player_2_up_pressed = False
player_2_down_pressed = False

# ball

ball_width = 10
ball_height = 10


ball_x = WIDTH/2      # Initial x position
ball_y = HEIGHT/2       # Initial y position
delta_x = 1       # change in x
delta_y = 1    # change in y

def on_update(delta_time):
   # player 1 movement
   global player_1_up_pressed, player_1_down_pressed, player_1_y

    # top border limit
   if player_1_y >= 684:
       player_1_y += 0
   elif player_1_up_pressed:
       player_1_y += 10

    # bottom border limit
   if player_1_y <= 36:
       player_1_y -= 0
   elif player_1_down_pressed:
       player_1_y -= 5


   # player 2 movement
   global player_2_up_pressed, player_2_down_pressed, player_2_y

    # top border limit
   if player_2_y >= 684:
       player_2_y += 0
   elif player_2_up_pressed:
       player_2_y += 5

    # bottom border limit
   if player_2_y <= 36:
       player_2_y -= 0
   elif player_2_down_pressed:
       player_2_y -= 5

    # ball movement
   global ball_x, ball_y
   global delta_x, delta_y

   ball_x += delta_x
   ball_y += delta_y

   # Figure out if we hit the edge and need to reverse.
   if ball_x < ball_height // 2 or ball_x > WIDTH - ball_width // 2:
       delta_x = -(delta_x*1.25)

   if ball_y < ball_height // 2 or ball_y > HEIGHT - ball_height // 2:
       delta_y = -delta_y



def on_draw():
   arcade.start_render()
   # player 1
   arcade.draw_rectangle_filled(player_1_x, player_1_y, 10, 72, arcade.color.BLUSH)

   # player 2
   arcade.draw_rectangle_filled(player_2_x, player_2_y, 10, 72, arcade.color.BLUSH)

   # ball
   arcade.draw_rectangle_filled(ball_x, ball_y, ball_width, ball_height, arcade.color.ALIZARIN_CRIMSON)


def on_key_press(key, modifiers):
   # player 1 key press
   global player_1_up_pressed, player_1_down_pressed, player_2_up_pressed, player_2_down_pressed

   if key == arcade.key.W:
       player_1_up_pressed = True

   elif key == arcade.key.S:
       player_1_down_pressed = True

   # player 2 key press
   if key == arcade.key.UP:
       player_2_up_pressed = True

   elif key == arcade.key.DOWN:
       player_2_down_pressed = True


def on_key_release(key, modifiers):
   # player 1 key release
   global player_1_up_pressed, player_1_down_pressed, player_2_up_pressed, player_2_down_pressed

   if key == arcade.key.W:
       player_1_up_pressed = False
   elif key == arcade.key.S:
       player_1_down_pressed = False

   # player 2 key release
   if key == arcade.key.UP:
       player_2_up_pressed = False

   elif key == arcade.key.DOWN:
       player_2_down_pressed = False


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
