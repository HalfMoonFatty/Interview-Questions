'''
Problem:

Design a Snake game that is played on a device with screen size = width x height. 

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
'''


'''
Solution:

__init__: constructor
    - snake is a Queue


isValid: helper fucntion
    - hit the border
    - the snake will bite itself

move fucntion:
    - calculate newHead according to the movement direction
    - check if the move is valid (poping out the tail first)
    - check if this move let the snake eat a food (newHead position == food[score] position)
        if eat a food: append the tail back to the RIGHT of the Queue; then add the newHead to the LEFT of the Queue.
        else: only add the newHead to the LEFT of the Queue.

        i.e.
        if eat food: pop current tail -> add the tail back --> add newHead --> the snake is increased by adding a newHead but the original is snake is the same.
        else: pop current tail --> add newHead --> the snake moved forwarded by 1.

** Note:
    As "each food appears one by one on the screen". So every time only consider the food indexed by score. e.g.
    initially, score == 0, then the ONLY food appears on the screen is food[0]
    after eating the first one, score = 1, then the next food appears on the screen is food[1]

'''


from collections import deque

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
            :type width: int
            :type height: int
            :type food: List[List[int]]
            """
        self.row = height
        self.col = width
        self.food = food
        self.snake = deque([[0,0]])
        self.score = 0


    def isValid(self, head):

        if head[0] < 0 or head[0] >= self.row or head[1] < 0 or head[1] >= self.col:
            return False
        for elem in self.snake:
            if elem[0] == head[0] and elem[1] == head[1]:
                return False
        return True



    def move(self, direction):
        """
            Moves the snake.
            @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
            @return The game's score after the move. Return -1 if game over.
            Game over when snake crosses the screen boundary or bites its body.
            :type direction: str
            :rtype: int
            """
        newHead = [self.snake[0][0],self.snake[0][1]]
        if direction == "U": newHead[0] -= 1
        elif direction == "L": newHead[1] -= 1
        elif direction == "R": newHead[1] += 1
        elif direction == "D": newHead[0] += 1

        # first pop the tail then check if the snake is valid
        tail = self.snake.pop()
        if not self.isValid(newHead): return -1

        # case 1: eat a food - add the tail back
        if self.score < len(self.food) and self.food[self.score] == newHead:
            self.score += 1
            self.snake.append(tail)

        # both case 1 and case 2 need to add newHead
        self.snake.appendleft(newHead)


        return self.score

