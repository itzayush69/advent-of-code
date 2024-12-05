import os

readme_path = 'README.md'
solutions_section = '## Solutions\n| Day | Puzzle | Part 1 Solution | Part 2 Solution |\n| --- | ------ | ---------------- | ---------------- |\n'

days = [d for d in os.listdir() if d.startswith('day_') and os.path.isdir(d)]
days.sort()

solutions = ''
for day in days:
    day_num = day.split('_')[1]
    part_1_py = f'{day}/part_1/solution.py'
    part_1_js = f'{day}/part_1/solution.js'
    part_2_py = f'{day}/part_2/solution.py'
    part_2_js = f'{day}/part_2/solution.js'
    puzzle_link = f'[Day {int(day_num)}](https://adventofcode.com/2024/day/{int(day_num)})'

    part_1_exists = os.path.exists(part_1_py) or os.path.exists(part_1_js)
    part_2_exists = os.path.exists(part_2_py) or os.path.exists(part_2_js)
    
    part_1_field = ''
    part_2_field = ''
    if part_1_exists:
        part_1_field = f'[Python]({part_1_py}) / [JavaScript]({part_1_js})'
    if part_2_exists:
        part_2_field = f'[Python]({part_2_py}) / [JavaScript]({part_2_js})'

    solutions += f'| {int(day_num)}  | {puzzle_link} | {part_1_field} | {part_2_field} |\n'

with open(readme_path, 'r') as file:
    lines = file.readlines()

with open(readme_path, 'w') as file:
    within_solutions_section = False
    for line in lines:
        if line.strip() == '## Solutions':
            file.write(line)
            file.write(solutions_section + solutions)
            within_solutions_section = True
        elif within_solutions_section and line.startswith('## '):
            within_solutions_section = False
            file.write(line)
        elif not within_solutions_section:
            file.write(line)