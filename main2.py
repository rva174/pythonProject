numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Numbers: ',numbers)
primes = []
not_primes = []
k = 0

for i in range(numbers[1], len(numbers) + 1):
    k = 1
    for j in range(2, i + 1):

        if i % j == 0:
            k = k + 1
    if k == 2:
        primes.append(i)
    if k > 2:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:',not_primes)


