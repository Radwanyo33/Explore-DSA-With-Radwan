n = int(input("Enter the length of the list:"))

arr = []
for i in range(n):
    element = input(f"Enter element no {i+1}: ")
    numbers = int(element)
    arr.append(numbers)
print("The input list before sorting: ", arr)

for i in range(n):
    min_idx = i
    for j in range (i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("The input list after sorting: ", arr)