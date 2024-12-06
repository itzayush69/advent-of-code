const fs = require('fs');

function countXmasCrosses(matrix) {
    let numbXMas = 0;
    for (let i = 1; i < matrix.length - 1; i++) {
        for (let j = 1; j < matrix[i].length - 1; j++) {
            if (matrix[i][j] === "A") {
                let tl_lr = matrix[i - 1][j - 1] + matrix[i + 1][j + 1];  // top left to bottom right
                let ll_tr = matrix[i + 1][j - 1] + matrix[i - 1][j + 1];  // bottom left to top right
                if (["SM", "MS"].includes(tl_lr) && ["SM", "MS"].includes(ll_tr)) {
                    numbXMas += 1;
                }
            }
        }
    }
    return numbXMas;
}

const lines = fs.readFileSync('../input.txt', 'utf8').trim().split('\n');
const matrix = lines.map(line => line.trim());

const result = countXmasCrosses(matrix);

console.log(`Answer: ${result}`);