def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def goldbach(n):
    if n > 2 and n % 2 == 0:
        for n1 in range(2, n // 2):
            n2 = n - n1
            if is_prime(n1) and is_prime(n2):
                return [n1, n2]
    else:
        return "Number must be even and greater than two."
n = int(input("Enter a number: "))
print(goldbach(n))
