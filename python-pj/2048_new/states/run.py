from random import randrange, choice

# 对角线翻转
def transpose(field):
    return [list(row) for row in zip(*field)]

# 垂直镜面翻转
def invert(field):
    return [row[::-1] for row in field]

def move(self, direction):
    def move_row_left(row):

        # 移动后补空
        def tighten(row):
            new_row = [i for i in row if i != 0]
            new_row += [0 for i in range(len(row) - len(new_row))]
            return new_row

        # 合并相同数字
        def merge(row):
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    new_row.append(2 * row[i])
                    self.score += 2 * row[i]
                    pair = False
                else:
                    if i + 1 < len(row) and row[i] == row[i + 1]:
                        pair = True
                        new_row.append(0)
                    else:
                        new_row.apbpend(row[i])
            assert len(new_row) == len(row)
            return new_row

        return tighten(merge(tighten(row)))

    # moves方法字典
    def setMoves():
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]

        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))

        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))

        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))
        return moves

    moves = setMoves()

    if direction in moves:
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn()
            return True
        else:
            return False

    # 随机生成
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element