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

    let isSafe = (increasing || decreasing) && validDifferences;

    if (!isSafe) {
        let isSafeAfterRemoval = false;

        for (let i = 0; i < report.length; i++) {
            const modifiedReport = [...report.slice(0, i), ...report.slice(i + 1)];

            increasing = true;
            decreasing = true;
            validDifferences = true;

            for (let j = 0; j < modifiedReport.length - 1; j++) {
                if (modifiedReport[j] > modifiedReport[j + 1]) {
                    increasing = false;
                }
                if (modifiedReport[j] < modifiedReport[j + 1]) {
                    decreasing = false;
                }
                if (!(1 <= Math.abs(modifiedReport[j] - modifiedReport[j + 1]) && Math.abs(modifiedReport[j] - modifiedReport[j + 1]) <= 3)) {
                    validDifferences = false;
                }
            }

            if ((increasing || decreasing) && validDifferences) {
                isSafeAfterRemoval = true;
                break;
            }
        }

        if (isSafeAfterRemoval) {
            safeCount += 1;
        }
    } else {
        safeCount += 1;
    }
}

console.log(`Answer: ${safeCount}`);