def sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
				

arr = map(int, input("Enter list items: ").split())

result = sort(list(arr))

print("Sorted array is:",*result)