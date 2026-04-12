num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
    
## Explanation:
'''The code takes a number as input from the user and checks if it is a palindrome. A palindrome is a number that reads the same backward as forward. The code uses string slicing to reverse the input number and compares it with the original number. If they are the same, it prints that the number is a palindrome; otherwise, it prints that it is not.

Here num[::-1] is a slicing operation that reverses the string. The [::-1] slice means to take the string and step through it backwards, effectively reversing it. The code then compares the original number (num) with the reversed version (num[::-1]) to determine if it is a palindrome.

Slice notation breakdown: [start:stop:step]
start - where to begin (empty = beginning)

stop - where to end (empty = end)

step - how to move (negative means go backwards)'''