def search(array,item):

    for i in range(len(array)):
        if array[i] == item:
            return i
    return None

array = map(int, input("Enter list items: ").split())
result = search(list(array), int(input("Enter a number to search: ")))

if result == None:
    print("Entered element not found.")
else:
    print("Entered element is found at position",result+1)