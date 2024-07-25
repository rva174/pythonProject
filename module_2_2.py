# if, elif. else
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
print(first)
print(second)
print(third)

if (first == second and first == third):
    print(3)
elif (second == first or second == third or first == third):
    print(2)
#elif (second != first and second != third or first != third):
#   print(0)
else:
    print(0)
