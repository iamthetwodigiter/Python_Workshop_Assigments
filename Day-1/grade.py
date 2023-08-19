m1 = int(input("enter marks 1: "))
m2 = int(input("enter marks 2: "))
m3 = int(input("enter marks 3: "))
m4 = int(input("enter marks 4: "))
m5 = int(input("enter marks 5: "))

avg = (m1+m2+m3+m4+m5)/5

if avg >= 60:
  print("Grade A")
elif avg>= 50 and avg <=59:
  print("Grade B")
elif avg>=40 and avg<=49:
  print("Grade C")
else:
  print("Fail")
