import random
import sys


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
    
    def draw_field(self):
        if self.col == 9:
            print('\n   123456789')
        elif self.col == 16:
            print('\n            1111111')
            print('   1234567890123456')
        elif self.col == 30:
            print('\n            111111111122222222223')
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
            
    def play(self):
        BOMB = 9
        OPEN = 2
        FLAG = 1
        try:
            row = int(input('Enter a row: '))
            col = int(input('Enter a column: '))
            act = int(input('Select an action: open(press 1), set flag(press 2), remove flag(press'
                            ' 3), quit(press q): '))
            while True:            
                if row >= 0 and row <= self.row and  col >= 0 and col <= self.col and act in (1, 2, 3, 4):
                    if act == 1:
                        self.field[row - 1][col - 1].open()
                        self.check_open_square()
                        if self.field[row - 1][col - 1].value != 0:
                            self.draw_field()
                        if self.field[row - 1][col - 1].value == BOMB:
                            print('\nBOMB! Game over!\n')
                            for i in range(self.row):
                                for j in range(self.col):
                                    if self.field[i][j].value == BOMB:
                                        self.field[i][j].open()
                            self.draw_field()
                            sys.exit(1)
                        if self.field[row - 1][col - 1].value == 0:
                            self.open_square(row - 1, col - 1)                            
                    elif act == 2:
                        self.field[row - 1][col - 1].set_flag()
                        self.check_open_square()
                        self.draw_field()
                    elif act == 3:
                        self.field[row - 1][col - 1].remove_flag()
                        self.draw_field()
                    elif act == 4:
                        for i in range(self.row - 1):
                            for j in range(self.col):
                                if self.field[i][j].value != BOMB:
                                        self.field[i][j].open()
                        self.draw_field()
                    else:
                        print('Input error. Try again.') 
                row = int(input('Enter a row: '))
                col = int(input('Enter a column: '))
                act = int(input('Select an action: open(press 1), set flag(press 2), remove flag' 
                                 '(press 3), quit(press q): '))
        except ValueError:
            print('Bye!')
            sys.exit(1)            
         
    def open_square(self, row, col):
        from collections import deque
        
        queue = deque()
        BOMB = 9
        CLOSE = 3
        while True:
            if row > 0:
                if col > 0:
                    if(self.field[row - 1][col - 1].value != BOMB and 
                       self.field[row - 1][col - 1].state == CLOSE):
                        if self.field[row - 1][col - 1].value == 0:
                            queue.append((row - 1, col - 1))
                        self.field[row - 1][col - 1].open()
                    if(self.field[row - 1][col].value != BOMB and 
                       self.field[row - 1][col].state == CLOSE):
                        if self.field[row - 1][col].value == 0:   
                            queue.append((row - 1, col))
                        self.field[row - 1][col].open()
            if col > 0:
                if(self.field[row][col - 1].value != BOMB and
                   self.field[row][col - 1].state == CLOSE):
                    if self.field[row][col - 1].value == 0:
                        queue.append((row, col - 1))
                    self.field[row][col - 1].open()
            if row != self.row - 1:
                if col > 0:
                    if(self.field[row + 1][col - 1].value != BOMB and 
                       self.field[row + 1][col - 1].state == CLOSE): 
                        if self.field[row + 1][col - 1].value == 0:                           
                            queue.append((row + 1, col - 1))
                        self.field[row + 1][col - 1].open()
                if col != self.col - 1:
                    if(self.field[row + 1][col + 1].value != BOMB and
                       self.field[row + 1][col + 1].state == CLOSE):
                        if self.field[row + 1][col + 1].value == 0:
                            queue.append((row + 1, col + 1))
                        self.field[row + 1][col + 1].open()
                    if(self.field[row + 1][col].value != BOMB and
                       self.field[row + 1][col].state == CLOSE):
                        if self.field[row + 1][col].value == 0:
                            queue.append((row + 1, col))
                        self.field[row + 1][col].open()
            if col != self.col - 1:
                if row > 0:
                    if(self.field[row - 1][col + 1].value != BOMB and
                       self.field[row - 1][col + 1].state == CLOSE):
                        if self.field[row - 1][col + 1].value == 0:
                            queue.append((row - 1, col + 1))
                        self.field[row - 1][col + 1].open()
                if(self.field[row][col + 1].value != BOMB and
                   self.field[row][col + 1].state == CLOSE):
                    if self.field[row][col + 1].value == 0:
                        queue.append((row, col + 1))
                    self.field[row][col + 1].open()
            if not queue:
                break
            else:
                row, col = queue.pop()
        self.draw_field()
        self.check_open_square()
        
    def check_open_square(self):
        OPEN = 2
        FLAG = 1
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.field[i][j].state == OPEN:
                    count += 1
        if count == self.row * self.col - self.bomb:
            for i in range(self.row):
                for j in range(self.col):
                    if self.field[i][j].state == FLAG:
                        self.field[i][j].remove_flag()
                        self.field[i][j].open()        
            self.draw_field()
            print('\nYou are a winner!!!')
            sys.exit(0)
        
                
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
        
    def remove_flag(self):
        if self.state == self.OPEN:
            return False 
        if self.state == self.FLAG:
            self.state = self.CLOSE 
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
                
              
def menu():
    print('Select level:')
    print('a) Beginner(9x9 field, 10 bombs)')
    print('b) Amateur(16x16 field, 40 bombs)')
    print('c) Professional(16x30 field, 99 bombs)')
    choice = input()
    while choice:
        if choice == 'a':
            return choice
        elif choice == 'b':
            return choice
        elif choice == 'c':
            return choice
        else:
            print('Invalid value. Try again:')
            choice = input()


if __name__ == '__main__':
    choice = menu()
    if choice == 'a':
        field = PlayingField(9, 9, 10)
    elif choice == 'b':
        field = PlayingField(16, 16, 40)
    elif choice == 'c':
        field = PlayingField(16, 30, 99)
    field.make_field()
    field.draw_field()
    field.play()
    