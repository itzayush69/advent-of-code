const fs = require('fs');

const memory = fs.readFileSync('../input.txt', 'utf8');

const pattern = /mul\((\d+),(\d+)\)/g;
let matches;
let totalSum = 0;

while ((matches = pattern.exec(memory)) !== null) {
    const x = parseInt(matches[1], 10);
    const y = parseInt(matches[2], 10);
    totalSum += x * y;
}

console.log("Answer:", totalSum);