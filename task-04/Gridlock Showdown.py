
def check_game_result(grid):

    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '.':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '.':
            return grid[0][i]
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.':
        return grid[0][2]
    
    return "DRAW"


def main():
    t = int(input())
    for _ in range(t):
        grid = [list(input().strip()) for _ in range(3)]
        result = check_game_result(grid)
        print(result)

if __name__ == "__main__":
    main()
