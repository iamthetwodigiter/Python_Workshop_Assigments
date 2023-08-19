choice = input("Enter 1 to convert from °C to °F or 2 to convert from °F to °C: ")

if choice == "1":
  degc = int(input("Enter your temperature in Celsius: "))
  degf = ((degc*9)/5)+32
  print("Temperature in degrees Farenheit is :",degf)

elif choice == "2":
  degreef = int(input("Enter your temperature in Farenheit: "))
  degreec = ((degreef - 32)/9)*5
  print("Temperature in degrees Celsius is :",degreec)

else:
  print("Invalid Input...")