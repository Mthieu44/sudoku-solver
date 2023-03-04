def solve_sudoku(puzzle):
    def is_valid(row, col, num):
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[box_row + i][box_col + j] == num:
                    return False
        return True

    def solver():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            puzzle[row][col] = num
                            if solver():
                                return True
                            puzzle[row][col] = 0
                    return False
        return True

    solver()

    return puzzle
