def is_even(num):
    if num % 2 == 0:
        return True
    return False

def luckynumber(number):
    num = [int(x) for x in str(number)]
    num = num[::-1]
    even_sum = 0
    odd_sum = 0
    for i in range(len(num)):
        if is_even(i):
            odd_sum += num[i]
        else:
            even_sum += num[i]
    if even_sum == odd_sum:
        return f'{number} is lucky number.'
    else:
        return f"{number} is not lucky number."

number = int(input("Enter a number: "))
print(luckynumber(number))