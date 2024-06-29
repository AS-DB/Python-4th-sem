#wap program to print twin prime number BETWEEN range of 1 to n digit.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(n):
    twin_pairs = []
    for i in range(2, 10 ** n):
        if is_prime(i) and is_prime(i + 2):
            twin_pairs.append((i, i + 2))
    return twin_pairs

n = int(input("Enter the number of digits (n): "))
print(f"Twin prime numbers up to {n} digits:")
for pair in twin_primes(n):
    print(pair)
