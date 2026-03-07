### Number Data Type Questions:

#1. Create a program that takes a float number as input and rounds it to 2 decimal places.

# n = float(input())
# print(round(n,2))

#2. Write a Python file that asks for three numbers and outputs the largest and smallest.

# a,b,c = map(int, input("Enter three numbers:").split())
# print("Max:",max(a,b,c))
# print("Min:", min(a,b,c))

#3. Create a program that converts kilometers to meters and centimeters.

# n = float(input("Enter leanth in km:"))

# print(f"n is {n*1000} meters")
# print(f"n is {n*100000} centimeters")

#4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
# a,b = map(int,input().split())
# x,y = divmod(a,b)
# print("integer division:", x,"\nthe remainder:", y)

#5. Make a program that converts a given Celsius temperature to Fahrenheit.

# a = float(input())

# print((a * (9/5)) + 32)

#6. Create a program that accepts a number and returns the last digit of that number.

# a = str(int(input()))
# print(a[-1])


#7. Create a program that takes a number and checks if it’s even or not.

# a = int(input())

# if a % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is not even")

### String Questions:

#1. Create a program to ask name and year of birth from user and tell them their age.

# name = input("Enter your name:")
# year = int(input("Enter your birth year"))

# print("Your age is :", 2026-year)

#2. Extract car names from this text:
# txt = 'LMaasleitbtui'

# car_name = txt[1:3]+txt[5]+txt[7]+txt[9]+txt[11]
# print(car_name)

# 4. Write a Python program to check if a given string is `palindrome` or not.

# n = input()

# if n[::-1] == n:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

#5. Write a program that counts the number of vowels and consonants in a given string.

# arr_vowels = "euioa"
# arr_consonants = "qwrtpsdfghjklzxcvbnmy"

# num_vowels:int = 0
# num_consonants:int = 0

# word = input()

# for i in word:
#     if i in arr_consonants:
#         num_consonants += 1
#     elif i in arr_vowels:
#         num_vowels +=1


# print("Number of vowels:", num_vowels)
# print("Number of cosonants:", num_consonants)

#6. Write a Python program to check if one string contains another.

# a = input("Enter string:")
# b = input("Enter another string:")

# if b in a  or a in b:
#     print("One string contains another")
# else:
#     print("One string doesn't contains another")

#7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.

# sen = input("Input sentence:")  
# rep = input("Replace:")
# wit = input("With:")

# sen = sen.replace(rep, wit)
# print(sen)

#8. Write a program that asks the user for a string and prints the first and last characters of the string.

# n = input()

# print("First character:", n[0], "\nLast character:", n[-1])

#9. Ask the user for a string and print the reversed version of it.

# n = input("Enter string:")
# print(n[::-1])

#10. Write a program that asks the user for a sentence and prints the number of words in it.

# n = input().split()

# print(len(n))

#11. Write a program to check if a string contains any digits.  

# n = input()

# num = "1234567890"
# bl: bool = True
# for i in num:
#     if i in n:
#         print("a string contains digits")
#         bl = False
#         break

# if bl:
#     print("a string doesn't contain digits")

#12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).

# n = input().split()
# ans = "-".join(n)
# print(ans)

#13. Ask the user for a string and remove all spaces from it.  

# n = input().split()
# ans = "".join(n)
# print(ans)

#14. Write a program to ask for two strings and check if they are equal or not.  

# a = input("First string:")
# b = input("Second string:")

# if a == b:
#     print("Those two strings are equal")
# else:
#     print("They are not equal")

#15. Ask the user for a sentence and create an acronym from the first letters of each word.  
    # Example:  
    # - Input: "World Health Organization"  
    # - Output: "WHO"  

# arr = input().split()
# ans = ""
# for i in arr:
#     ans += i[0]
# print(ans)


#16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  

# arr = input("Enter a string:")
# n = input("Enter a charecter:")

# ans = ""
# for i in arr:
#     if i is not n:
#         ans += i

# print(ans)

#17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`). 
# 

# n = input("Enter a string:")

# arr_vowels = "euioya"

# ans = ""
# for i in n:
#     if i not in arr_vowels:
#         ans += i
#     else:
#         ans += "*"

# print(ans)

#18. Write a program that checks if a string starts with one word and ends with another.  

# n = input("Enter string:").split()

# print("Starts with:", n[0])
# print("Ends with:", n[-1])

### Boolean Data Type Questions:

#1. Write a program that accepts a username and password and checks if both are not empty.

# username = input()
# password = input()

# if username and password:
#     print("They are not empty")
# else:
#     print("They are empty")

#2. Create a program that checks if two numbers are equal and outputs a message if they are.

# a, b = map(int, input().split())

# if a == b:
#     print("This two numbers are equal")
# else:
#      print("They are not equal")

#3. Write a program that checks if a number is positive and even.

# n = int(input())

# if n >= 0 and n % 2 == 0:
#     print("This number is even  and  positive")
# else:
#     print("This is not")

#4. Write a program that takes three numbers and checks if all of them are different.

# a,b,c = map(int, input("Enter tree numbers:").split())

# if a != b and b != c and a != c:
#     print("They are different")
# else:
#     print("at least 2 of them is same")

#5. Create a program that accepts two strings and checks if they have the same length.

# a = input()
# b = input()

# if len(a) == len(b):
#     print("They have the same length")
# else:
#     print("They don't have the same length")


#6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

# a =  int(input())

# if a % 3 == 0 and a % 5 == 0:
#     print("it's divisible by both 3 and 5")

# else:
#     print("it isn't divisible by both 3 and 5")

#7. Write a program that checks if the sum of two numbers is greater than 50.

# a , b = map(int, input().split())

# if a+b > 50:
#     print("the sum of two numbers is greater than 50")
# else:
#     print("the sum of two numbers is not greater than 50")


# #8. Create a program that checks if a given number is between 10 and 20 

# a = int(input())

# if  10 <= a and a <= 20:
#     print("number is between 10 and 20")
# else:
#     print("number is not between 10 and 20")