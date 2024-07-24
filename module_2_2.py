# if, elif. else
first = 256
second = 457
third = 850
print(first)
print(second)
print(third)

if (first == second and first == third):
    print(3)
elif (second == first or second == third or first == third):
    print(2)
elif (second != first and second != third or first != third):
    print(0)
else:
    print(0)
