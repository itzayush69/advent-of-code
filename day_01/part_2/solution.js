const fs = require("fs");

fs.readFile("../input.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    const lines = data.split("\n");

    const list1 = [];
    const list2 = [];

    lines.forEach(line => {
        const parts = line.trim().split(/\s+/).filter(part => part).map(Number);

        if (parts.length === 2) {
            list1.push(parts[0]);
            list2.push(parts[1]);
        }
    });

    let similarity_score = 0;
    list1.forEach(num => {
        const count_in_list2 = list2.filter(x => x === num).length;
        similarity_score += num * count_in_list2;
    });

    console.log("Answer:", similarity_score);
});
