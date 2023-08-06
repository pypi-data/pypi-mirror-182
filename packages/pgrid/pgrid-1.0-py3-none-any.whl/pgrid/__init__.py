import pygame

class cell():

    def __init__(self, Position: tuple, Value: int = 0, Direction: tuple = None, Distance: float = None):
        self.Position = Position
        self.Value = Value
        self.Direction = Direction
        self.Distance = Distance
    
    def modify(self, Value: int = None, Direction: tuple = None, Distance: float = None):
        if Value != None:
            self.Value = Value
        if Direction != None:
            self.Direction = Direction
        if Distance != None:
            self.Distance = Distance

class board():
    widthPixels = None
    cellsPerLine = None
    Colors = None

    data: list [cell] = []
    def __init__(self, widthPixels: int = 500, cellsPerLine: int = 20, Colors = [(255,255,255),(255,0,0),(0,255,0),(0,0,255)]):
        self.widthPixels = widthPixels
        self.cellsPerLine = cellsPerLine
        self.Colors = Colors
      # Setup first time data:
        for i in range(cellsPerLine**2):
            cell_ = cell(Position=(i%cellsPerLine,i//cellsPerLine), Value=0)
            self.data.append(cell_)
    
    def find(self, xPos, yPos):
        desiredCell = cell((0,0),0)
        for x in self.data:
            if x.Position == (xPos,yPos):
                desiredCell = x
        return desiredCell
    
    def drawBoard(self, Screen):
        squerePixel = self.widthPixels/self.cellsPerLine
      # Color the background
        for cell_ in self.data:
            rect = pygame.Rect(cell_.Position[0]*squerePixel, cell_.Position[1]*squerePixel, squerePixel, squerePixel)
            pygame.draw.rect(Screen, self.Colors[cell_.Value], rect)

      # Draw the lines
        blockSize = int(self.widthPixels/self.cellsPerLine)
        for x in range(0, int(self.widthPixels), blockSize):
            for y in range(0, int(self.widthPixels), blockSize):
                rect = pygame.Rect(x,y, blockSize, blockSize)
                pygame.draw.rect(Screen, (0,0,0), rect, 1)

