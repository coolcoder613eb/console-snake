from random import randint
import os
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep
import sys
# 12x16

def on_press(key):
    if key == Key.right:
        return right()
    elif key == Key.left:
        return left()
    elif key == Key.up:
        return up()
    elif key == Key.down:
        return down()
    else:
        return True

def up():
    global di
    if di == 'right' or di == 'left':
        di = 'up'
        return False
    else:
        return True


def down():
    global di
    if di == 'right' or di == 'left':
        di = 'down'
        return False
    else:
        return True


def right():
    global di
    if di == 'up' or di == 'down':
        di = 'left'
        return False
    else:
        return True

def left():
    global di
    if di == 'up' or di == 'down':
        di = 'right'
        return False
    else:
        return True

def check():
    x = [num[0],num[1]]
    n = snake.pop()
    snake.append(n)
    for i in range(len(snake)-2):
        if x == snake[i]:
            gameover()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def gameover():
    input('Game Over!\nPress Enter to continue... ')
    sys.exit()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def app():
    global apple; apple = [randint(0,11),randint(0,11)]

def move():
    global num, score, scorev
    if di =='left':
        if num[1] != 11:
            num[1] += 1
            snake.append([num[0],num[1]])
        else:
            num[1] = 0
            snake.append([num[0],num[1]])
        
        x = [num[1],num[1]]
        
        if x == apple:
            app()
            score += 1
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
            
    if di =='right':
        if num[1] != 0:
            num[1] -= 1
            snake.append([num[0],num[1]])
        else:
            num[1] = 11
            snake.append([num[0],num[1]])
        x = [num[0],num[1]]
        if x == apple:
            app()
            score += 1
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
    if di =='up':
        if num[0] != 0:
            num[0] -= 1
            snake.append([num[0],num[1]])
        else:
            num[0] = 15
            snake.append([num[0],num[1]])
        x = [num[0],num[1]]
        if x == apple:
            app()
            score += 1
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
    if di =='down':
        if num[0] != 15:
            num[0] += 1
            snake.append([num[0],num[1]])
        else:
            num[0] = 0
            snake.append([num[0],num[1]])
        x = [num[0],num[1]]
        if x == apple:
            app()
            score += 1
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
    refresh()
    check()
    sleep(0.4)

def refresh():
    global apple, rows
    rows = [[p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p],
            [p,p,p,p,p,p,p,p,p,p,p,p]]
    cls()
    

    for x in snake:
        rows[x[0]][x[1]] = s

        
    rows[apple[0]][apple[1]] = a

    print(scorev)
    print(h*(len(rows[0])+2))
    for row in rows:
        print(h,end = '')
        for item in row:
            print(item,end = '')
        print(h,end = '')
        print('')
    print(h*(len(rows[0])+2))
    print(r)



s = "\u001b[32mo "
a = "\u001b[31mό "
h = "\u001b[34m# "
r = "\u001b[0m"
g = "\u001b[90m"
p = r+'+ '
c = g+'V '
p = c

rows = [[p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p],
        [p,p,p,p,p,p,p,p,p,p,p,p]]




snake = []
snake.append([6,8]); snake.append([5,8])
apple = [randint(0,11),randint(0,11)]

num = [5,8]

score = 0
scorev = 'Score: '+str(score)
di = 'up'

paused = False

for x in snake:
    rows[x[0]][x[1]] = s
rows[apple[0]][apple[1]] = a

print('')
print(h*(len(rows[0])+2))
for row in rows:
    print(h,end = '')
    for item in row:
        print(item,end = '')
    print(h,end = '')
    print('')
print(h*(len(rows[0])+2))
print(r)


listener = keyboard.Listener(on_press=on_press)
listener.start()
while not paused:
    move()
input('Press Enter to continue . . . ')
