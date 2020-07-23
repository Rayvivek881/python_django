maze = [[1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1]]


def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def isSafe(x, y, N):
    return 0 <= (x and y) < N and maze[x][y]


def solveMaze(N):
    sol = [[0 for j in range(N)] for i in range(N)]
    if solveMazeUtil(0, 0, sol, N) is False:
        print("Solution doesn't exist")
        return False
    printSolution(sol)
    return True


def solveMazeUtil(x, y, sol, N):
    if x == y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if isSafe(x, y, N):
        sol[x][y] = 1
        if solveMazeUtil(x + 1, y, sol, N):
            return True
        if solveMazeUtil(x, y + 1, sol, N):
            return True
        sol[x][y] = 0
        return False


solveMaze(5)