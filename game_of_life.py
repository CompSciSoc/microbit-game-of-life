from microbit import *

def grid_to_image(grid):
    return Image("".join(["".join(map(str, row))+':' for row in grid]))

def display_as_grid():
    return [[display.get_pixel(x, y) for x in range(5)] for y in range(5)]
    
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
            
x, y = 0, 0
pixel = 0

def move():
    global x, y
    x += 1
    if x == 5:
        x, y = 0, y+1
    if y == 5:
        y = 0

GLIDER = [
    [0,0,0,0,0],
    [0,0,9,0,0],
    [0,0,0,9,0],
    [0,9,9,9,0],
    [0,0,0,0,0],
]

display.show(grid_to_image(GLIDER))
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.set_pixel(x, y, pixel)
        grid = display_as_grid()
        while button_a.is_pressed() and button_b.is_pressed():
            grid = tick(grid)
            display.show(grid_to_image(grid))
            sleep(200)
            
            # reset was_pressed to `False`, this happens whenever it is called
            _, _ = button_a.was_pressed(), button_b.was_pressed()
        pixel = display.get_pixel(x, y)
    
    if button_a.was_pressed():
        display.set_pixel(x, y, pixel)
        move()
        pixel = display.get_pixel(x, y)

    if button_b.was_pressed():
        display.set_pixel(x, y, 9-pixel)
        move()
        pixel = display.get_pixel(x, y)

    if accelerometer.was_gesture('shake'):
        grid = GLIDER
        display.show(grid_to_image(grid))

    display.set_pixel(x, y, 9)
    sleep(200)
    display.set_pixel(x, y, 0)
    sleep(200)
