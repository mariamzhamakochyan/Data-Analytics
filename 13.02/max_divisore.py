def div(num):
    res = 0
    for i in range(2, num):
        if num % i == 0:
            res += 1
    return res

def max_div(a,b):
    if a <= b:
        dict = {}
        keys = dict.keys()
        for i in range(a, b+1):
            divisors = div(i)
            dict.update({i:divisors});
        return max(dict, key=dict.get)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f'The most number of divisors has {max_div(a,b)}')
