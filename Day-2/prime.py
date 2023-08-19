def prime(n):
    flag = False
    i = 2
    while i < n//2:
        if n % i == 0:
            flag = True
        i += 1
    
    if flag:
        print("Number is not Prime")
    else:
        print("Number is Prime.")

prime(int(input("Enter a number: ")))