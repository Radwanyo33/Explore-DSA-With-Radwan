num = int(input("Enter a number: "))

original = num

palindrome = 0

while num>0:
    remainder = num%10
    palindrome = palindrome*10 + remainder
    num = num//10

if original == palindrome:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is not a palindrome number.")

# num_str = input("Enter a number: ")
# num = int(num_str)  # Still convert for math operations
# original = num
# palindrome = 0
# temp = num

# while temp > 0:
#     remainder = temp % 10
#     palindrome = palindrome * 10 + remainder
#     temp = temp // 10

# # Check BOTH conditions
# if num == palindrome and num_str == num_str[::-1]:
#     print(f"{num_str} is a palindrome")
# elif num_str != num_str[::-1] and num == palindrome:
#     print(f"{num_str} has leading zeros, but {num} is a palindrome")
# else:
#     print(f"{num_str} is not a palindrome")