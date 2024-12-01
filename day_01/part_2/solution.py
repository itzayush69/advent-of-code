with open("../input.txt", 'r') as file:
    lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, filter(None, line.strip().split(' '))))
        if len(numbers) == 2:
            list1.append(numbers[0])
            list2.append(numbers[1])

    similarity_score = 0
    for num in list1:
        count_in_list2 = list2.count(num)
        similarity_score += num * count_in_list2

    print("Answer:", similarity_score)