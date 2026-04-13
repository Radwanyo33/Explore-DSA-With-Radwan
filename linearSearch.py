n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = input(f"Enter element no {i+1}: ")
    numbers = int(element)
    arr.append(numbers)
print("The input array: ", arr)

search = int(input("Enter the element to be searched: "))
for i in range(n):
    if arr[i] == search:
        print(f"Element {search} is found at index {i} and position {i+1}")
        break
    else: 
        if i == n-1:
            print(f"Element {search} is not found in the array")