# Sorting Started here. Binary search requires sorted array. So, we will sort the array first and then apply binary search on it.
n = int(input("Enter the number of array elements: "))

arr = []
for i in range(n):
    element = input(f"Enter element no {i+1}: ")
    numbers = int(element)
    arr.append(numbers)
print("Array before sorting: ", arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
print("Array after sorting: ", arr) 
# Sorting algorithm ends.
search = int(input("Enter the element to be searched: "))
low = 0
high = n-1
found = False
while low <= high:
    mid = (low+high)//2
    if arr[mid] == search:
        print(f"Element {search} is found at index {mid} and position {mid+1}")
        found = True
        break
    elif arr[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print(f"Element {search} is not found in the list")
print("Thanks for using the program.........")