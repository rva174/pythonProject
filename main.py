#1st programm
print((9 ** 0.5) * 5)
#2nd programm
print(9.99 > 9.98 and 1000 != 1000.1)
#3rd programm
print((1234 // 10) % 100)     # 23
print((5678 // 10) % 100)     # 67
print((1234 // 10) % 100 + (5678 // 10) % 100)   # 90
#4th programm
print(int(13.42))                            # 13
print(int((13.42 * 100) % 100))            # 42
print(int(42.13))                             # 42
print(int((42.13 * 100) % 100))               # 13
print(int(13.42) == int((42.13 * 100)) % 100) or int(42.13) == int((13.42 * 100) % 100)

#4th programm (вариант)
a1 = int(13.42)
print(a1)                                #13
a2 = int((13.42 * 100) % 100)
print(a2)                                  # 42
b1 = int(42.13)
print (b1)                                  # 42
b2 = int((42.13 * 100) % 100)
print (b2)                                   #13
print(a1 == b2) or (a2 == b1)
