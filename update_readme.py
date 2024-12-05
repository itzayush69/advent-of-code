import os

def update_readme():
    readme_path = 'README.md'
    solutions_section = '## Solutions\n| Day | Puzzle | Part 1 Solution | Part 2 Solution |\n| --- | ------ | ---------------- | ---------------- |\n'
    
    days = [d for d in os.listdir() if d.startswith('day_') and os.path.isdir(d)]
    days.sort()
    
    solutions = ''
    for day in days:
        day_num = day.split('_')[1]
        part_1_py = f'[{day}/part_1/solution.py]'
        part_1_js = f'[{day}/part_1/solution.js]'
        part_2_py = f'[{day}/part_2/solution.py]'
        part_2_js = f'[{day}/part_2/solution.js]'
        puzzle_link = f'[Day {int(day_num)}](https://adventofcode.com/2024/day/{int(day_num)})'
        solutions += f'| {int(day_num)}  | {puzzle_link} | [Python]({part_1_py}) / [JavaScript]({part_1_js}) | [Python]({part_2_py}) / [JavaScript]({part_2_js}) |\n'
    
    with open(readme_path, 'r') as file:
        lines = file.readlines()
    
    with open(readme_path, 'w') as file:
        for line in lines:
            if line.strip() == '## Solutions':
                file.write(solutions_section + solutions)
                break
            file.write(line)

if __name__ == '__main__':
    update_readme()