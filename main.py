import numpy as np
import time

sudoku = np.array([0, 0, 0, 2, 6, 0, 7, 0, 1,
                   6, 8, 0, 0, 7, 0, 0, 9, 0,
                   1, 9, 0, 0, 0, 4, 5, 0, 0,
                   8, 2, 0, 1, 0, 0, 0, 4, 0,
                   0, 0, 4, 6, 0, 2, 0, 0, 0,
                   0, 5, 0, 0, 0, 3, 0, 2, 8,
                   0, 0, 9, 3, 0, 0, 0, 7, 4,
                   0, 4, 0, 0, 5, 0, 0, 3, 6,
                   7, 0, 3, 0, 1, 8, 0, 0, 0], int)
sudoku_matrix = sudoku.copy().reshape((9, 9))

start_time = time.time()

solved = False
impossible = False
iterations = 0
while not solved:
    iterations += 1
    if iterations > 30000:
        impossible = True
        break
    solved = True
    for pos, num in enumerate(sudoku):
        pos_x = pos % 9
        pos_y = pos // 9
        if num == 0:
            solved = False
            possible_numbers = []
            for possible in range(1, 10):
                if possible not in sudoku_matrix[pos_y, :]:
                    if possible not in sudoku_matrix[:, pos_x]:
                        block_x = pos_x // 3
                        block_y = pos_y // 3
                        if possible not in sudoku_matrix[block_y * 3: block_y * 3 + 3, block_x * 3: block_x * 3 + 3].flatten():
                            possible_numbers.append(possible)
            if len(possible_numbers) == 1:
                sudoku[pos] = possible_numbers[0]
                sudoku_matrix = sudoku.copy().reshape((9, 9))


if impossible:
    print("No solution found... :C")
print(sudoku_matrix)
print(f"Took me {time.time() - start_time} seconds!")
