const fs = require('fs');

const lines = fs.readFileSync('../input.txt', 'utf8').split('\n');

const grid = lines.map(line => line.trim());
const word = "XMAS";
const rows = grid.length;
const cols = grid[0].length;
const wordLen = word.length;

const directions = [
    [0, 1],    // right
    [0, -1],   // left
    [1, 0],    // down
    [-1, 0],   // up
    [1, 1],    // diagonal down right
    [1, -1],   // diagonal down left
    [-1, 1],   // diagonal up right
    [-1, -1]   // diagonal up left
];

let count = 0;

function isValid(x, y) {
    return 0 <= x && x < rows && 0 <= y && y < cols;
}

for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
        for (const [dr, dc] of directions) {
            let match = true;
            for (let k = 0; k < wordLen; k++) {
                const nr = r + dr * k;
                const nc = c + dc * k;
                if (!isValid(nr, nc) || grid[nr][nc] !== word[k]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                count += 1;
            }
        }
    }
}

console.log("Answer:", count);
