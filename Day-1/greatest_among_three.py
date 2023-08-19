a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b:
  max = a
elif b>a:
  max = b

if max<c:
  max = c
print("Maximum among the three numbers is = ",max)
