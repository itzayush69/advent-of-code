def count_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # diagonal down right
        (1, -1),   # diagonal down left
        (-1, 1),   # diagonal up right
        (-1, -1)   # diagonal up left
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                match = True
                for k in range(word_len):
                    nr, nc = r + dr * k, c + dc * k
                    if not is_valid(nr, nc) or grid[nr][nc] != word[k]:
                        match = False
                        break
                if match:
                    count += 1

    return count


with open("../input.txt", "r") as file:
    grid = [line.strip() for line in file]

result = count_word(grid, "XMAS")

print(f"Answer: {result}")
