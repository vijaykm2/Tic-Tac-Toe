prime_numbers = [2,3]

for i in range(4, 1001):

    checks = [i % j != 0 for j in range(2, i-1)]
    isPrime = all(checks)
    if isPrime:
        prime_numbers.append(i)

# print(prime_numbers)