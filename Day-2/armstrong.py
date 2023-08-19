def armstrong(n):
    sum = 0
    for i in list(n):
        sum += int(i)**3

    if sum == int(n):
        print(f"{n} is Armstrong Number.")
    else:
        print(f"{n} is not Armstrong Number.")

armstrong(input("Enter a number: "))