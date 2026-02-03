import random


class PlayingField:
    
    def __init__(self, row, col, bomb):
        if row not in (9, 16) or col not in (9, 16, 30) or bomb not in (10, 40, 99):
            raise ValueError('Invalid value')
        else:
            self.row = row
            self.col = col
            self.bomb = bomb
            self.field = []
            for i in range(self.row):
                self.field.append([Square(0) for _ in range(self.col)])
            """self.field[5][6].set_flag()
            self.field[8][8].bomb()
            self.field[8][8].open()
            self.field[7][8] = Square(1)
            self.field[7][8].open()"""
    
    def draw_field(self):
        if self.col == 9:
            print('   123456789')
        elif self.col == 16:
            print('            1111111')
            print('   1234567890123456')
        elif self.col == 30:
            print('            111111111122222222223')
            print('   123456789012345678901234567890')
        print()
        for i in range(self.row):
            if i < 9:
                print(f' {i + 1}', end=' ')
            if i >= 9:
                print(f'1{i - 9}', end=' ')                 
            for j in range(self.col):
                self.field[i][j].draw()
            print()
    
    def make_field(self):
        BOMB = 9
        coordinates = []
        bomb_list = []
        for i in range(self.row):
            for j in range(self.col):
                coordinates.append((i,j))
        bomb_list = random.sample(coordinates, self.bomb)
        for i, j in bomb_list:
            self.field[i][j].bomb()
            
        for i in range(self.row):
            for j in range(self.col):
                if self.field[i][j].value == BOMB:
                    continue
                if i > 0:
                    if j > 0 and self.field[i - 1][j - 1].value == BOMB:
                        self.field[i][j].value += 1
                    if self.field[i - 1][j].value == BOMB:
                        self.field[i][j].value += 1
                if j > 0:
                    if self.field[i][j - 1].value == BOMB:
                        self.field[i][j].value += 1
                if i != self.row - 1:
                    if j > 0 and self.field[i + 1][j - 1].value == BOMB:
                        self.field[i][j].value += 1
                    if j != self.col - 1 and self.field[i + 1][j + 1].value == BOMB:
                        self.field[i][j].value += 1
                    if self.field[i + 1][j].value == BOMB:
                        self.field[i][j].value += 1
                if j != self.col - 1:
                    if i > 0 and self.field[i - 1][j + 1].value == BOMB:
                        self.field[i][j].value += 1
                    if self.field[i][j + 1].value == BOMB:
                        self.field[i][j].value += 1
            
        for i in range(self.row):
            for j in range(self.col): 
                self.field[i][j].open()
                
                
class Square:
    FLAG = 1
    OPEN = 2
    CLOSE = 3
    BOMB = 9
        
    def __init__(self, value: int = 0):
        self.state = self.CLOSE 
        self.value = value
            
    def open(self):
        if self.state == self.FLAG:
            return False
        self.state = self.OPEN
        return True
    
    def set_flag(self):
        if self.state == self.OPEN:
            return False        
        self.state = self.FLAG
        return True
        
    def bomb(self):
        self.value = self.BOMB
        return True
        
    def draw(self):
        if self.state == self.OPEN:
            if self.value == self.BOMB:
                print('*', end='')
            else:
                print(self.value, end='')
        else:
            if self.state == self.FLAG:
                print('F', end='')
            else:
                print('?', end='')


if __name__ == '__main__':
   # random.seed()
    """print('Select level:')
    print('a) Beginner(9x9 field, 10 bombs')
    print('b) Amateur(16x16 field, 40 bombs')
    print('c) Professional(16x30 field, 99 bombs')
    choice = input()
    while is choice:
        if choice == a:
            field = PlayingField(9, 9, 10)
            break
        elif choice == b:
            field = PlayingField(16, 16, 40)
            break
        elif choice == c:
            field = PlayingField(16, 30, 99)
            break
        else:
            print('Invalid value. Try again:')
            choice = input()
    row = int(input('Enter a row: '))
    col = int(input('Enter a column: '))
    act = int(input('Select an action: open(press 1), set flag(press 2)'))
        
    x = PlayingField(12, 16, 40)
    x.draw_field()
    
                
        """
    """s = Square(9)
    print(s.bomb())
    s.open()
    s.draw()
    s1 = Square(9)
    s1.set_flag()
    s1.draw()
    s2 = Square(1)
    s2.open()
    s2.draw()
    s3 = Square(2)
    s3.draw()
    s4 = Square(0)
    s4.open()
    s4.draw()"""
    x = PlayingField(16, 16, 40)
    x.make_field()
    x.draw_field()
    
    
    