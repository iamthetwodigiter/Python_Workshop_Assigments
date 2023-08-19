def factorial(n):
    if n > 0:
        return factorial(n-1) * n
    else:
        return 1

def peterson(n):
    sum = 0
    for i in list(n):
        sum += factorial(int(i))

    if sum == int(n):
        print(f"{n} is a Peterson Number.")
    else:
        print(f"{n} is not a Peterson Number.")

peterson(input("Enter a number: "))