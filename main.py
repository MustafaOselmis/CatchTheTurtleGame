import turtle
import random
import time

i = 0


def clickTurtle(x, y):
    global i
    i += 1
    t.clear()
    t.write(f"Your Score : {i}", font=("Arial", 30, "normal"))


a = turtle.Turtle()
a.penup()
a.hideturtle()
a.setposition(30, 250)

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.setposition(-50, 200)

drawing_Board = turtle.Screen()
drawing_Board.bgcolor("light blue")
drawing_Board.title("Kaplumbağayı Yakala")

bob = turtle.Turtle()
bob.shape("turtle")
bob.penup()
bob.onclick(clickTurtle)

direction = [0, 90, 180, 270]
moving = [10, 20, 30]

is_paused = False


def toggle_pause():
    global is_paused
    is_paused = not is_paused


time_limit = 5
start_time = time.time()

while True:
    if not is_paused:
        bob.forward(random.choice(moving))
        bob.setheading(random.choice(direction))

        elapsed_time = time.time() - start_time
        remaining_time = time_limit - int(elapsed_time)
        print(remaining_time)


        a.clear()
        a.write(f'Remaining Time : {remaining_time}', font=("Arial", 30, "normal"))

        if remaining_time <= 0:
            print("GAME OVER")
            drawing_Board.bye()
            break
    else:
        drawing_Board.update()

turtle.done()