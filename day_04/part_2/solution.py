def count_xmas_crosses(matrix):
    numb_x_mas = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if matrix[i][j] == "A":
                tl_lr = matrix[i-1][j-1] + matrix[i+1][j+1]  # top left to bottom right
                ll_tr = matrix[i+1][j-1] + matrix[i-1][j+1]  # bottom left to top right
                if all(diag in ("SM", "MS") for diag in [tl_lr, ll_tr]):
                    numb_x_mas += 1
    return numb_x_mas


with open("../input.txt", "r") as file:
    matrix = [line.strip() for line in file]

result = count_xmas_crosses(matrix)

print(f"The number of X-MAS patterns in the grid is {result}.")
