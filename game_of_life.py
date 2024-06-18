from microbit import *

def grid_to_image(grid):
    return Image("".join(["".join(map(str, row))+':' for row in grid]))

def tick(grid):
    new = [ [0]*5 for _ in range(5) ]
    for x in range(5):
        for y in range(5):
            count = sum(
                [grid[i%5][j%5] for i, j in 
                [(x-1,y), (x-1,y-1), (x,y-1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1)]
            ])//9

            if count == 3: new[x][y] = 9
            elif count == 2 and grid[x][y]: new[x][y] = 9
            else: new[x][y] = 0
     
    return new
            
grid = [
    [0,0,0,0,0],
    [0,0,9,0,0],
    [0,0,0,9,0],
    [0,9,9,9,0],
    [0,0,0,0,0],
]

x, y = 0, 0
pixel = 0

def move():
    global x, y
    x += 1
    if x == 5:
        x, y = 0, y+1
    if y == 5:
        y = 0
        
display.show(grid_to_image(grid))
while True:
    while button_a.is_pressed() and button_b.is_pressed():
    

        sleep(200)
        grid = tick(grid)

    if button_a.was_pressed():
        display.set_pixel(x, y, pixel)
        move()
        pixel = display.get_pixel(x, y)

    if button_b.was_pressed():
        if pixel == 9:
            display.set_pixel(x, y, 0)
        else:
            display.set_pixel(x, y, 9)
            
        move()
        pixel = display.get_pixel(x, y)

    display.set_pixel(x, y, 9)
    sleep(200)
    display.set_pixel(x, y, 0)
    sleep(200)
