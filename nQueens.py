sol = 0

def calculate(N):
    queens_positions = [-1] * N
    place_queen(N, queens_positions, 0)
    print("Number of solutions: ", sol)

def place_queen(N, queens_positions, current_row):
        if current_row == N:
            global sol
            sol += 1
        else:
            for column in range(0, N):
                if verify(queens_positions, current_row, column):
                    queens_positions[current_row] = column
                    place_queen(N, queens_positions, current_row + 1)

def verify(pos, rows, column):
        for i in range(0, rows):
            if pos[i] == column or pos[i] - i == column - rows or pos[i] + i == column + rows:
                return False
        return True



def main():
    N = int(input('N: '))
    calculate(N)

if __name__ == "__main__":
    main()