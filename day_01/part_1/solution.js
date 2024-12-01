const fs = require("fs");

fs.readFile("../input.txt", "utf8", (err, data) => {
    if (err) {
        console.error("err in reading the file:", err);
        return;
    }

    const lines = data.split("\n");

    const list1 = [];
    const list2 = [];

    lines.forEach(line => {
        const numbers = line.trim().split(/\s+/).filter(n => n).map(Number);

        if (numbers.length === 2) {
            list1.push(numbers[0]);
            list2.push(numbers[1]);
        }
    });

    list1.sort((a, b) => a - b);
    list2.sort((a, b) => a - b);

    let totalDistance = 0;
    for (let i = 0; i < Math.min(list1.length, list2.length); i++) {
        totalDistance += Math.abs(list1[i] - list2[i]);
    }

    console.log("Answer:", totalDistance);
});