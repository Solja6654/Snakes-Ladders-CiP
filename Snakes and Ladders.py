import turtle
import random



TILE_SIZE = 60
START_X = -270
START_Y = -270
positions = [0,0]
player_colours = ['red', 'blue']
ladders = {1:24, 5:30, 19:37, 35:48, 39: 63, 45: 67, 61: 89}
snakes = {23:2, 38:12, 41: 16, 52:42, 78:47, 91: 77, 99: 57}





def create_board():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.speed(0)
    number = 1
    for i in range(10):
        for j in range(10):
            if i % 2 == 0:
                x = START_X + j * TILE_SIZE
            else:
                x = START_X + (9 - j) * TILE_SIZE
            y = START_Y + i * TILE_SIZE
            drawer.goto(x, y)
            if number % 2 == 0:
                drawer.fillcolor("orange")
                drawer.begin_fill()
            drawer.pendown()
            for k in range(4):
                drawer.forward(TILE_SIZE)
                drawer.left(90)
            if number % 2 == 0:
                drawer.end_fill()
            drawer.penup()
            drawer.goto(x + 5, y + 5)
            drawer.write(str(number), font=("Times New Roman", 8, "normal"))
            number += 1

def get_position(position):
    if position == 0:
        return START_X - TILE_SIZE, START_Y - TILE_SIZE
    row = (position-1) // 10
    col = (position-1) % 10
    if row % 2 ==1:
        col = 9 - col
    x = START_X + col * TILE_SIZE + TILE_SIZE // 2
    y = START_Y + row * TILE_SIZE + TILE_SIZE // 2
    return x, y

def move_player(player_turtle, player_index):
    roll = random.randint(1, 6)
    print(f"{player_names[player_index]} rolled a {roll}!")
    new_position = positions[player_index] + roll
    if new_position > 100:
        return
    if new_position in ladders:
        print(f"Climbed ladder from {new_position} to {ladders[new_position]}")
        new_position = ladders[new_position]
    elif new_position in snakes:
        print(f"Fell due to snake from {new_position} to {snakes[new_position]}")
        new_position = snakes[new_position]
    positions[player_index] = new_position
    x, y = get_position(new_position)
    player_turtle.goto(x, y)



def main():
    global player_names
    screen = turtle.Screen()
    screen.title("Snakes and Ladders")
    screen.setup(700, 700)
    Player1_name = turtle.textinput("Player 1", "Enter name for Player 1 (Red):") or "Player 1"
    Player2_name = turtle.textinput("Player 2", "Enter name for Player 2") or "Player 2"
    player_names = [Player1_name, Player2_name]
    create_board()
    turtles = []
    for color in player_colours:
        t = turtle.Turtle()
        t.shape("circle")
        t.color(color)
        t.penup()
        t.speed(0)
        t.goto(get_position(0))
        turtles.append(t)
    current_player = [0]
    def play_turn():
        move_player(turtles[current_player[0]], current_player[0])
        if positions[current_player[0]] == 100:
            print(f"Player {player_names[current_player[0]]} wins!")
            turtle.bye()
            return
        current_player[0] = 1 - current_player[0]
        screen.ontimer(play_turn, 1500)
    screen.ontimer(play_turn, 1500)
    turtle.done()
    screen.mainloop()










if __name__ == "__main__":
    main()
