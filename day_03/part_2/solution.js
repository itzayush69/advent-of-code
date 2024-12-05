const fs = require('fs');

const memory = fs.readFileSync('../input.txt', 'utf8');

const pattern = /(do\(\)|don't\(\)|mul\((\d+),(\d+)\))/g;
let matches;
let totalSum = 0;
let enabled = true;

while ((matches = pattern.exec(memory)) !== null) {
    const instruction = matches[0];

    if (instruction === "do()") {
        enabled = true;
    } else if (instruction === "don't()") {
        enabled = false;
    } else {
        if (enabled) {
            const x = parseInt(matches[2], 10);
            const y = parseInt(matches[3], 10);
            totalSum += x * y;
        }
    }
}

console.log("Answer:", totalSum);