class PlayingField:
    
    def __init__(self, row, col, bomb):
        mark = False
        if row not in (9, 16):
            mark = True
        elif col not in (9, 16, 30):
            mark = True
        elif bomb not in (10, 40, 99):
            mark = True
        if mark == True:
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


class Square(PlayingField):
        
        def __init__(self, row, col, bomb):
            PlayingField.__init__(self, row, col, bomb)
            for i in range(self.row):
                for j in range(self.col):
                    self.board[i][j] = None
        
        def seed_bombs(self):
            BOMB = 9
            numbers_bomb = self.bomb
            while is numbers_bomb:
                self.board[random.randint(0, self.row)][random.randint(0, self.col)] = BOMB
                numbers_bomb -= 1
        
        def init_square(self):
            all_bomb = 0 
            for i in range(self.row):
                for j in range(self.col):
                    if self.board[i][j] == BOMB:
                            continue
                    if i > 0:
                        if self.board[i - 1][j] == BOMB:
                            all_bomb += 1
                    if j > 0:
                        if self.board[i][j - 1] == BOMB:
                            all_bomb += 1
                    if i not self.row - 1:
                        if self.board[i + 1][j] == BOMB:
                            all_bomb += 1
                    if j not self.col - 1:
                        if self.board[i][j + 1] == BOMB:
                            all_bomb += 1
                    if all_bomb > 0:
                        self.board[i][j] = all_bomb
                    else:
                        self.board[i][j] = 0                  
                all_bomb = 0
                            
            


if __name__ == '__main__':
    random.seed()
    x = PlayingField(12, 16, 40)
    x.draw_field()
                
        
    