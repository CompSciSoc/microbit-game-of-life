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

while True:
    display.show(grid_to_image(grid))
    sleep(200)
    grid = tick(grid)
