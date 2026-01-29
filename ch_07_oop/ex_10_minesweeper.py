class PlayingField:
    
    def __init__(self, row, col, bomb):
        if row not in (9, 16) or col not in (9, 16, 30) or bomb not in (10, 40, 99):
            raise ValueError('Invalid value')
        else:
            self.row = row
            self.col = col
            self.bomb = bomb
    
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
            for j in range(self.col + 3):
                if j == 0 and self.row == 9:
                    print(' ', end='')
                elif j == 1 and self.row == 9:
                    print(i + 1, end='')
                elif j == 0 and self.row == 16:
                    if i <= 8:
                        print(' ', end='')
                    else:
                        print('1', end='')
                elif j == 1 and self.row == 16:
                    if i <= 8:
                        print(i + 1, end='')
                    else:
                        print(i - 9, end='')
                elif j == 2:
                    print(' ', end='')
                else:
                    print('?', end='')
            print()
    
    def make_field(self):
        for i in range(self.row):
            for j in range(self.col):
                self.field[i][j] = Square()   
        BOMB = 9
        numbers_bomb = self.bomb
        bomb_row = random.sample(range(0, self.row), numbers_bomb)
        bomb_col = random.sample(range(0, self.col), numbers_bomb)
        for i, j in bomb_row, bomb_col:
            self.field[i][j] = Square.bomb()
        all_bomb = 0 
        for i in range(self.row):
            for j in range(self.col):
                if self.field[i][j] == BOMB:
                        continue
                if i > 0:
                    if self.field[i - 1][j] == BOMB:
                        all_bomb += 1
                if j > 0:
                    if self.field[i][j - 1] == BOMB:
                        all_bomb += 1
                if i not self.row - 1:
                    if self.field[i + 1][j] == BOMB:
                        all_bomb += 1
                if j not self.col - 1:
                    if self.field[i][j + 1] == BOMB:
                        all_bomb += 1
                if all_bomb > 0:
                    self.field[i][j] = all_bomb
                else:
                    self.field[i][j] = 0                  
            all_bomb = 0
        
    

class Square:
    FLAG = 1
    OPEN = 2
    CLOSE = 3
    BOMB = 9
        
    def __init__(self, value: int = 0):
        self.state = CLOSE 
        self.value = value
            
    def open(self):
        if self.state == FLAG:
            return False
        self.state = OPEN
        return True
    
    def set_flag(self):
        if self.state == OPEN:
            return False        
        self.state = FLAG
        return True
        
    def bomb(self):
        self.value = BOMB
        return True
        
    def draw_square(self):
        if self.state == OPEN:
            if self.value == BOMB:
                print('💣')
            elif self.value == FLAG:
                print('🚩')


if __name__ == '__main__':
    random.seed()
    print('Select level:')
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
                
        
    