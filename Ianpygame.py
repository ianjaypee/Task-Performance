import turtle
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Obstacle Dodger")  # Updated game title
wn.bgcolor("lightgray")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off the screen updates for performance

# Create the player car
car = turtle.Turtle()
car.shape("square")
car.color("blue")
car.penup()
car.speed(0)
car.shapesize(stretch_wid=1, stretch_len=2)  # Made the car smaller
car.sety(-250)

# Create the obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    # Choose a random shape for the obstacle
    shapes = ["square", "circle", "triangle"]
    shape = random.choice(shapes)
    obstacle.shape(shape)
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.shapesize(stretch_wid=1, stretch_len=2)
    obstacle.setx(random.randint(-290, 290))
    obstacle.sety(300)
    obstacles.append(obstacle)

# Variables to handle movement
moving_left = False
moving_right = False

def start_left():
    global moving_left
    moving_left = True

def stop_left():
    global moving_left
    moving_left = False

def start_right():
    global moving_right
    moving_right = True

def stop_right():
    global moving_right
    moving_right = False

def move_car():
    if moving_left:
        x = car.xcor()
        if x > -290:  # Adjust boundary to allow for gradual movement
            car.setx(x - 1)  # Move left very slowly

    if moving_right:
        x = car.xcor()
        if x < 290:  # Adjust boundary to allow for gradual movement
            car.setx(x + 1)  # Move right very slowly

# Keyboard bindings
wn.listen()
wn.onkeypress(start_left, "Left")
wn.onkeyrelease(stop_left, "Left")
wn.onkeypress(start_right, "Right")
wn.onkeyrelease(stop_right, "Right")

# Main game loop
score = 0
initial_speed = 0.5  # Set initial speed to be very slow
speed = initial_speed

# Create initial obstacles (decreased number)
for _ in range(3):
    create_obstacle()

while True:
    wn.update()
    
    move_car()  # Check and move the car based on key presses
    
    # Move obstacles
    for obstacle in obstacles:
        obstacle.sety(obstacle.ycor() - speed)
        
        # Reset obstacle position if it goes off-screen
        if obstacle.ycor() < -300:
            obstacle.hideturtle()
            obstacles.remove(obstacle)
            create_obstacle()  # Create a new obstacle
            score += 10  # Increase score
            print(f"Score: {score}")
        
        # Check for collision with the car
        if car.distance(obstacle) < 30:  # Adjust collision distance for smaller car
            print(f"Game Over! Final Score: {score}")
            turtle.bye()  # Close the window
            break

    # Increase speed gradually
    if score % 50 == 0 and score > 0:  # Increase speed every 50 points
        speed = initial_speed + (score // 50) * 0.05  # Increase speed by 0.05
        if speed > 2:  # Cap the maximum speed to avoid excessive difficulty
            speed = 2
