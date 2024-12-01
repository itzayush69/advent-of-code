with open("../input.txt", 'r') as file:
    lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, filter(None, line.strip().split(' '))))
        if len(numbers) == 2:
            list1.append(numbers[0])
            list2.append(numbers[1])

    list1.sort()
    list2.sort()

    total_distance = sum(abs(num1 - num2) for num1, num2 in zip(list1, list2))

    print("Answer:", total_distance)