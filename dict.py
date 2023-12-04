weak = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье'
}
print(weak.get(1))
weak.pop(3)
for i in weak:
    print(weak.get(i))

key = weak.keys()
value = weak.values()
items = weak.items()
print(key)
print(value)
print(items)
