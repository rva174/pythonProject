my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('my_list: ', my_list)
numbers = len(my_list)
print('Количество элементов в списке: ', numbers)

number = 0  # Индекс элемента списка, от 0 до (numbers - 1)

while(number <= (numbers) - 1):
    print(my_list[number])
    number = number + 1
    if my_list[number] < 0:
        break
print('Перебор элементов списка завершен')






