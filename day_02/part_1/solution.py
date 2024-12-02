safe_count = 0

with open("../input.txt", 'r') as file:
    for line in file:
        report = list(map(int, line.strip().split()))
        
        increasing = True
        decreasing = True
        valid_differences = True

        for i in range(len(report) - 1):
            if report[i] > report[i + 1]:
                increasing = False
            if report[i] < report[i + 1]:
                decreasing = False
            if not (1 <= abs(report[i] - report[i + 1]) <= 3):
                valid_differences = False

        if (increasing or decreasing) and valid_differences:
            safe_count += 1

print(f"Answer: {safe_count}")