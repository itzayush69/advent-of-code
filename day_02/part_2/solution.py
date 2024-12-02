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

        is_safe = (increasing or decreasing) and valid_differences

        if not is_safe:
            is_safe_after_removal = False
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]

                increasing = True
                decreasing = True
                valid_differences = True

                for j in range(len(modified_report) - 1):
                    if modified_report[j] > modified_report[j + 1]:
                        increasing = False
                    if modified_report[j] < modified_report[j + 1]:
                        decreasing = False
                    if not (1 <= abs(modified_report[j] - modified_report[j + 1]) <= 3):
                        valid_differences = False

                if (increasing or decreasing) and valid_differences:
                    is_safe_after_removal = True
                    break

            if is_safe_after_removal:
                safe_count += 1
        else:
            safe_count += 1

print(f"Answer: {safe_count}")