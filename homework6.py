my_dict = {'Владимир': 1870, 'Fedor': 2000, 'Анна': 2002}
print(type(my_dict))
print('Dict:', my_dict)
print(my_dict['Владимир']) # Вывод значения по существующему ключу
print(my_dict.get('Байден')) # Ключ отсутствует
my_dict.update({'Petr': 2001,
               'Maria': 2016})
print('Modificed dictionary:', my_dict)
a = my_dict.pop('Fedor')
print('Deleted value:', a)
print('Modificed dictionary:', my_dict)

my_set = {1, 3, 6, 'dog', 'cat'}
print('My_set:', my_set)
my_set.add(5)
my_set.add('goal')
print('Modificired my_set:', my_set)
my_set.discard(3)
print('Modificired my_set:', my_set)









