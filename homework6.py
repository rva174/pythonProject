immutable_var = True, 'urban', 5, 10.5
print(type(immutable_var))
print('immutable_var:',immutable_var)
#immutable_var[0] = True
#immutable_var[1] = 25
#immutable_var[-1] = 10
print('immutable_var:',immutable_var)
#Элементы кортежа неизменяемые
mutable_list = ['table', 'chair', 'sofa', 3]
print('mutable_list:', mutable_list)
mutable_list.append(True)
print('mutable_list:', mutable_list)
print('Добавлен элемент в конец списка')
mutable_list.extend('goal')
print('mutable_list:', mutable_list)
print('Символы строк goal добавлены по одному')
mutable_list.extend(['goal', 4])
mutable_list[0] = 'desk'
print('mutable_list:', mutable_list)
print('Строка goal не разобрана на символы,она здесь элемент списка,')
print('      заменен перрвый элемент списка')
mutable_list.remove('chair')
print('mutable_list:', mutable_list)
print('  Элемент chair  исключен из списка')
print('  Элемент chair  исключен из списка')