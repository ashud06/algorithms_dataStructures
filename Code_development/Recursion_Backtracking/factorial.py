n=5

def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

ans = factorial(n)
print('factorial of {0} is {1}'.format(n, ans))