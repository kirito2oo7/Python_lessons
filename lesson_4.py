## Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# 2.  What is the difference between the continue and break statements in Python?
# break = stops loop completely
# continue = skips and moves to next loop iteration.
# 3. Can you explain the difference between for loop and while loop? 3. Can you explain the difference between for loop and while loop?
# for loop used in situations where iteration are known (list, set, dict ...)
# while loop runs while a condition is true.
# 4. How would you implement a nested for loop system? Provide an example.

# for i in range(10):        
#     for j in range(10):    
#         print(i, j)




### Homework

# **1.** Return uncommon elements of lists. Order of elements does not matter.

# list1 = [int(i) for i in input("list1 = ").split()]
# list2 = [int(i) for i in input("list2 = ").split()]



# result = []

# for i in list1:
#     if i not in list2:
#         result.append(i)

# for j in list2:
#     if j not in list1:
#         result.append(j)

# print(result)

#**2.** Print the square of each number which is less than `n` on a separate line.

# n = int(input("N = "))

# for i in range(1,n):
#     print(i**2)

#**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


txt = input()
vowels = "aeiouAEIOU"

result = ""
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1

    if count == 3 and i != len(txt) - 1:
        if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == "_"):
            count -= 1
        else:
            result += "_"
            count = 0

print(result)



# txt = input()
# list_unli = "aiuoe"
# ans = ""
# for i in range(len(txt)):
#     ans += txt[i]
#     if (i+1)%3 == 0 and (txt[i] not in list_unli):
#         ans += "_"
    


#**4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.



# from random import randint

# def game():
#     random_guess = randint(1,100)
    
#     for i in range(10):
#         number = int(input("Enter number between 1 to 100: "))
#         if number == random_guess:
#             print("You have guessed it right!")
#             break
#             return
#         elif number > random_guess:
#             print("Too high!")
#         else:
#             print("Too low!")
    
#     ans = input("You lost. Want to play again? ")
#     arr = ["Y", "y", "YES", "yes", "ok"]
#     if ans in arr:
#         game()

# game()
# print("Game end!")



# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."


# password = input("Enter password:")
# ans = ""
# lower_password = password.lower()
# if len(password) < 8:
#     ans += "Password is too short "
#     if lower_password == password:
#         ans += "and password must contain an uppercase letter."
# elif lower_password == password:
#     ans += "Password must contain an uppercase letter."
# else:
#     ans = "Password is strong."

# print(ans)

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# def is_prime(number):
#     for x in range(2,int(number**(0.5))):
#         if number % x == 0:
#             return False
#     return True

# arr = []
# for i in range(2,100):
#     if is_prime(i):
#         arr.append(i)
# print(*arr)


# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.




### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.

# import random

# hand = input("Please enter `rock`, `paper`, or `scissors`: ")
# arr = ["rock", "paper", "scissors"]
# point_hand = 0
# point_comp = 0
# comp_hand = arr[random.randint(0,2)]


# # h= 0 and c = 1 # comp wins -1
# # h= 0 and c = 2 # hand  wins -2
# # h= 1 and c = 0 # hand wins 1
# # h= 1 and c = 2 # comp wins -1
# # h= 2 and c = 0 # comp wins 2
# # h= 2 and c = 1 # hand wins 1

# hand_win = [-2, 1]
# comp_win = [-1, 2]
# while point_comp < 5 and point_hand < 5:
#     print("Computer entered:",comp_hand)
    
#     if  arr.index(hand) - arr.index(comp_hand) in hand_win:
#         point_hand += 1
#     elif arr.index(hand) - arr.index(comp_hand) in comp_win:
#         point_comp += 1
#     else:
#         pass
#     print(f"Result:{point_hand}:{point_comp}")
#     hand = input("Please enter `rock`, `paper`, or `scissors`: ")
    
#     comp_hand = arr[random.randint(0,2)]

# print(f"Result:{point_hand}:{point_comp}")