from random import randint
import os
from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from time import sleep
import sys
# 12x16

def on_press(key):
    #if not paused:
    if key == Key.right:
        return right()
    elif key == Key.left:
        return left()
    elif key == Key.up:
        return up()
    elif key == Key.down:
        return down()
##    elif key == KeyCode(char = 'p'):
##        print('foo\n'*3)
##        return pause()
    else:
        return True
##    if key == KeyCode(char = 'p'):
##        print('bar\n'*3)
##        return pause()

def pause():
    global paused
    if paused:
        paused = False
        return True
    else:
        paused = True
        return False

def cut():
    global cutthere
    o = int((len(snake))/2)
    for k in range(o):
        snake.pop(0)
    cutthere = False
    scissor = [360,360]

def sci():
    global scissor, cutthere
    cutthere = True
    scissor = [randint(0,11),randint(0,11)]

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
            if (score % 6) == 0:
                print('a\n'*1000)
                sci()
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
        if x == scissor:
                    cut()
            
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
            if (score % 6) == 0:
                print('a\n'*1000)
                sci()
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
        if x == scissor:
                    cut()
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
            if (score % 6) == 0:
                print('a\n'*1000)
                sci()
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
        if x == scissor:
                    cut()
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
            if (score % 6) == 0:
                print('a\n'*1000)
                sci()
            scorev = 'Score: '+str(score)
        else:
            snake.pop(0)
        if x == scissor:
                    cut()
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
    if cutthere:
        rows[scissor[0]][scissor[1]] = c

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
p = p

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



cutthere = False
scissor = [360,360]
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
while True:

    while not paused:
        move()

input('Press Enter to continue . . . ')
