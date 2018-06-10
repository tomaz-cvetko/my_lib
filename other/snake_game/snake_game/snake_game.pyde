from Snake import Snake
from Snake import Position



def setup():
    size(400, 400)
    frameRate(50)
    background(0)
    
    colorMode(RGB, 100)
    global bg
    bg = color(0, 0, 0)
    
    global snake
    snake = Snake()
    snake.food.reset()
    
def draw():
    background(bg)
    snake.update()
    snake.show()
    snake.food.show()
    
def keyPressed():
    if key == CODED:
        if keyCode == UP:
            snake.makeTurn(Position(0, -1))
        elif keyCode == DOWN:
            snake.makeTurn(Position(0, 1))
        elif keyCode == LEFT:
            snake.makeTurn(Position(-1, 0))
        elif keyCode == RIGHT:
            snake.makeTurn(Position(1, 0))