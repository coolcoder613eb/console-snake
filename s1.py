from pynput import keyboard
import os
import time

# Define initial variables
rows = []
width = 20
height = 20
r = 0
c = 0
dir = 'right'
food = [7,6]
snake = [[0,0]]
h = '-'

# Define the function to update the snake's position
def move():
    global r, c, dir, food, snake

    # Update the snake's head based on the direction
    if dir == 'right':
        c += 1
    elif dir == 'left':
        c -= 1
    elif dir == 'up':
        r -= 1
    elif dir == 'down':
        r += 1

    # Check if the snake has hit the boundaries
    if c == width or c < 0 or r == height or r < 0:
        print("Game Over")
        os._exit(1)

    # Check if the snake has eaten the food
    if [r,c] == food:
        food = []
        while food == []:
            food = [
                int(random.randrange(1, height-1, 1)),
                int(random.randrange(1, width-1, 1))
            ]
            if food in snake:
                food = []
    else:
        snake.pop()

    # Check if the snake has hit itself
    if [r,c] in snake:
        print("Game Over")
        os._exit(1)
    
    snake.insert(0, [r,c])

# Define the function to change the direction based on keyboard input
def on_press(key):
    global dir
    if key == keyboard.Key.left:
        dir = 'left'
    elif key == keyboard.Key.right:
        dir = 'right'
    elif key == keyboard.Key.up:
        dir = 'up'
    elif key == keyboard.Key.down:
        dir = 'down'

# Set up the listener for keyboard input
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Generate the initial food position
while food == []:
    food = [
        int(random.randrange(1, height-1, 1)),
        int(random.randrange(1, width-1, 1))
    ]
    if food in snake:
        food = []

# Create the initial rows for the game board
for i in range(height):
    rows.append([])
    for j in range(width):
        if i == 0 or i == height-1 or j == 0 or j == width-1:
            rows[i].append('X')
        elif [i,j] in snake:
            rows[i].append('O')
        elif [i,j] == food:
            rows[i].append('F')
        else:
            rows[i].append(' ')

print(rows)
print(snake)
print(food)

# Run the game loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the game board
    #print('')
    #print(' '.join(([h] * (len(rows[0]) + 2))))
    for row in rows:
        print(' '.join(row))
