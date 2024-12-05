import re

file_path = '../input.txt'
with open(file_path, 'r') as file:
    memory = file.read()

pattern = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")
matches = pattern.findall(memory)

total_sum = 0
enabled = True

for match in matches:
    instruction = match[0]
    
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            x = int(match[1])
            y = int(match[2])
            total_sum += x * y

print("Answer:", total_sum)
