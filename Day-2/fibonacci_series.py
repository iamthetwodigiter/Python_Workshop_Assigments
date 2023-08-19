#Version 1
def fibonacci(n):
    series = [0,1]
    for i in range(n):
            item = series[i-2] + series[i-1]
            series.append(item)

    print(*series)

fibonacci(int(input("Enter a number: ")))

#Version 2
def fibonacci(n):
    series = [0,1]
    for i in range(2,n):
        # if i > 1:
            item = series[i-2] + series[i-1]
            series.append(item)

    print(*series)

fibonacci(int(input("Enter a number: ")))