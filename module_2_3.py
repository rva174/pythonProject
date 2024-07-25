my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('my_list: ',my_list)
numbers = len(my_list)
print('Количество элементов в списке: ',numbers)

number = 0               # индекс первого элемента списка, от 0 до 11
print(my_list[number])   #

while number <= ((numbers) - 1):
    if my_list[number] < 0:
        print('Отрицательное число: ',my_list[number])
    number = number + 1
else:
    print ('Перебор элементов списка завершен')






