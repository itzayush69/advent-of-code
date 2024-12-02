const fs = require("fs");

let safeCount = 0;

const fileContent = fs.readFileSync("../input.txt", "utf8");
const lines = fileContent.trim().split("\n");

for (let line of lines) {
    const report = line.split(" ").map(Number);

    let increasing = true;
    let decreasing = true;
    let validDifferences = true;

    for (let i = 0; i < report.length - 1; i++) {
        if (report[i] > report[i + 1]) {
            increasing = false;
        }
        if (report[i] < report[i + 1]) {
            decreasing = false;
        }
        if (!(1 <= Math.abs(report[i] - report[i + 1]) && Math.abs(report[i] - report[i + 1]) <= 3)) {
            validDifferences = false;
        }
    }

    if ((increasing || decreasing) && validDifferences) {
        safeCount += 1;
    }
}

console.log(`Answer: ${safeCount}`);