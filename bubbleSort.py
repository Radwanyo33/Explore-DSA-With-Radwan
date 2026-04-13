n = int(input("Enter the number of array elements: "))

arr = []
for i in range(n):
    element = input("Enter the elements one by one: ")
    numbers = int(element)
    arr.append(numbers)
print("Array before sorting: ", arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
print("Array after sorting: ", arr) 
