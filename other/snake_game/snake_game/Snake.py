class Position:
    def __init__(self, xpos = 0, ypos = 0):
        self.x = xpos
        self.y = ypos
        
class Food:
    def __init__(self):
        self.location = Position(-1, -1)
        self.kind = color(80, 20, 5)
        self.r = 7
        
    def reset(self):
        self.location = Position(random(width), random(height))
        
    def show(self):
        stroke(self.kind)
        ellipse(self.location.x, self.location.y, self.r, self.r)
    

class Snake:
    def __init__(self):
        self.head = Position(width/2, height/2)
        self.body = []
        
        self.currentSize = 200
        self.speed = 3
        self.thickness = 9
        
        self.velocity = Position(1, 0)
        self.body.append(Position(0, height/2))
        
        self.kind = color(0, 90, 10)
        self.food = Food()
        
    def newTurn(self):
        self.body.insert(0, self.head)

        
    def checkDir(self, aDirection):
        if self.velocity.x == 0 and aDirection.y == 0 and aDirection.x != 0:
            return True
        elif self.velocity.y == 0 and aDirection.x == 0 and aDirection.y != 0:
            return True
        else:
            return False
        
    
    def makeTurn(self, aDirection):
        if self.checkDir(aDirection):
            self.newTurn()
            self.velocity = aDirection
        
    
    @staticmethod    
    def dist(aPosition, bPosition):
        return abs(aPosition.x - bPosition.x)+abs(aPosition.y - bPosition.y)
    
    @staticmethod
    def dir(aPosition, bPosition):
        
        if aPosition.x < bPosition.x:
            return Position(1, 0)
        elif aPosition.x > bPosition.x:
            return Position(-1, 0)
        elif aPosition.y > bPosition.y:
            return Position(0, -1)
        elif aPosition.y < bPosition.y:
            return Position(0, 1)
        else:
            return Position(100, 100)
    
    @staticmethod    
    def plus(aPosition, factor, direction):
        return Position(aPosition.x + factor*direction.x, aPosition.y + factor*direction.y)
    
    def moveAhead(self):
        self.head = Snake.plus(self.head, self.speed, self.velocity)
        
    def checkCollision(self):
        
        for i in range(3, len(self.body)):
            first = self.body[i-1]
            position = self.body[i]
             
            # postarska metrika to the rescue
            headDiff = Snake.dist(self.head, first) + Snake.dist(self.head, position)
            minDiff = Snake.dist(first, position) + 2*self.thickness
            
            if (headDiff) <= (minDiff):
                return True
            else:
                return False
            
    def checkFood(self):
        
        a = sq(self.head.x - self.food.location.x) + sq(self.head.y - self.food.location.y)
        if a <= sq(self.food.r):
            return True
        else:
            return False

    
    # WORK ORGANISERS:    
    def update(self):
        self.moveAhead()
        
        if self.checkCollision():
            self.speed = 0
            print("GameOver!")
            
        if self.checkFood():
            print("Hit the Food!")
            self.food.reset()
            self.currentSize += 10
            
        
        
    def show(self):
        
        #set drawing parameters
        stroke(self.kind)
        strokeWeight(self.thickness)
        
        tailDrawn = 0
        first = self.head
        #print("show")
        
        s = 'The head Position is: (' + repr(self.head.x)+ ', ' + repr(self.head.y) + ')\n'
        #print(s)
        
        for originalPosition in self.body:
            
            position = originalPosition
            
            
            #calculate how much is the distance to next turn and how
            #much still has to be drawn
            diff = Snake.dist(first, position)
            restOfTail = self.currentSize - tailDrawn
            
            #this is how the last line is drawn
            if(restOfTail < diff):
                whereTo = Snake.dir(first, position)
                
                position = Snake.plus(first, restOfTail, whereTo)
                index = self.body.index(originalPosition)
                self.body.pop(index)
                self.body.insert(index, position)
                
                
                tailDrawn = self.currentSize + 1
            else:
                tailDrawn += diff
            
            
            #draw on canvas
            line(first.x, first.y, position.x, position.y)
            
            
            if tailDrawn >= self.currentSize:
                #end drawing and clear the unnecessary turns
                eraseStart = self.body.index(position)
                if len(self.body) > 1:
                    for i in range(len(self.body) - eraseStart - 1):
                        self.body.pop()
                break
                
            first = originalPosition