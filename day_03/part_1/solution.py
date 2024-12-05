import re

with open("../input.txt", 'r') as file:
    memory = file.read()

pattern = re.compile(r'mul\((\d+),(\d+)\)')
matches = pattern.findall(memory)

total_sum = 0
for match in matches:
    x = int(match[0])
    y = int(match[1])
    total_sum += x * y

print("Answer:", total_sum)
