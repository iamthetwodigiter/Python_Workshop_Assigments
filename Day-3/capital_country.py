dataset = {
    "Afghanistan":"Kabul",
    "Albania":"Tirana",
    "Algeria":"Algiers",
    "Andorra":"Andorra la vella",
    "India":"New Delhi",
    "Pakistan":"Islamabad",
    "Bangladesh":"Dhaka"
}

country = input("Enter country name: ")

capital = dataset.get(country,"Capital not found.")

print(capital)