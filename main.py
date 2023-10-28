import array as arr


class frstArray:
    frstArray = arr.array("i", [1, 2, 3, 4, 5, 6])
    sncdArray = arr.array("i", [13, 45, 64])

    print("Первый массив:")
    for a in frstArray:
        print(a)
    print()

    print("Второй массив:")
    for i in sncdArray:
        print(i)

    frstArray.append(10)
    print("Добавили число 10 в конец массива:")
    for a in frstArray:
        print(a)
    print()

    frstArray.insert(0, 12)
    print("Добавили число 12 в начало массива так-же вместо 0 можно использовать любое числа не превышающий длину массива")
    for a in frstArray:
        print(a)
    print()

    frstArray.pop(3)
    print("Удалили 3й элемент из массива так-же вместо 3 можно использовать любое числа не превышающий длину массива")
    for a in frstArray:
        print(a)
    print()

    frstArray.extend(sncdArray)
    print("Объеденим 2 массива:")
    for a in frstArray:
        print(a)
