from orm import QueenCase, Solution, session

sol = 0
first_time = False


def solution_exists(N):
    exist = session.query(QueenCase).filter_by(n=N).count()
    if exist == 0:
        return False
    return True


def calculate(N):
    queens_positions = [-1] * N
    place_queen(N, queens_positions, 0)
    print("Number of solutions: ", sol)

    if first_time:
        queen_case = session.query(QueenCase).filter_by(n=N).first()
        queen_case.number_of_solutions = sol
        session.commit()
    else:
        queen_case = QueenCase(n=N, number_of_solutions=sol)
        session.add(queen_case)
        session.commit()
        

def place_queen(N, queens_positions, current_row):
        if current_row == N:
            solution = str(queens_positions).strip('[]')
            solution = solution.replace(' ', '')

            if not solution_exists(N):
                global first_time
                first_time = True
                queen_case = QueenCase(n=N, number_of_solutions=0)
                session.add(queen_case)
                session.commit()

            if first_time:
                query = session.query(QueenCase).filter_by(n=N)
                for x in query:
                    queen_case_id = x.id
                
                sol_obj = Solution(queen_case_id=queen_case_id, solution=solution)
                session.add(sol_obj)
                session.commit()

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
