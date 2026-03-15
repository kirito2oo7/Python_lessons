#Task 1

# def convert_cel_to_far(number):
#     return round(number * 9/5 + 32,2)

# def convert_far_to_cel(number):
#     return round((number - 32) * 5/9,2)

# number = int(input("Enter a temperature in degrees F: "))
# print(f"{number} degrees F = {convert_far_to_cel(number):.2f} degrees C")

# number2 = int(input("Enter a temperature in degrees C: "))
# print(f"{number2} degrees C = {convert_cel_to_far(number2):.2f} degrees F")

#Task 2

# def invest(amount, rate, years):
#     ans = ""

#     for i in range(years):
#         ans += f"year {i+1}: ${(amount + amount*rate):.2f}\n"
#         amount = amount + amount*rate
    
#     return ans

# print(invest(100, .05, 4))

#Task 3

# number = int(input("Enter a positive integer: "))

# for i in range(1,number+1):
#     if number % i == 0:
#         print(f"{i} is a factor of {number}")

#Task 4

# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]


# def enrollment_stats(list_of_university):
#     total_student = 0
#     total_tuition = 0
#     for university in list_of_university:
#         total_student += university[1]
#         total_tuition += university[2]

#     return [total_student , total_tuition]


# def mean(list_of_university):
#     total_student_mean = enrollment_stats(universities)[0] / len(list_of_university)
#     total_Tuition_mean = enrollment_stats(universities)[1] / len(list_of_university)
#     return [total_student_mean , total_Tuition_mean ]

# def median(list_of_university):
#     list_student = []
#     for i in list_of_university:
#         list_student.append(i[1])

#     list_student.sort()
#     student_median = list_student[len(list_student)//2]

#     list_Tuition  = []
#     for j in list_of_university:
#         list_Tuition.append(j[2])

#     list_Tuition.sort()
#     Tuition_median = list_Tuition[len(list_Tuition)//2]

#     return [student_median , Tuition_median]


# txt = f"""******************************
# Total students: {enrollment_stats(universities)[0]}
# Total tuition: $ {enrollment_stats(universities)[1]}

# Student mean: {mean(universities)[0]:.2f}
# Student median: {median(universities)[0]}

# Tuition mean: $ {mean(universities)[1]:.2f}
# Tuition median: $ {median(universities)[1]}
# ******************************"""

# print(txt)

#Task 5

# def is_prime(number):
#     for x in range(2,int(number**(0.5))):
#         if number % x == 0:
#             return False
#     return True

# number = int(input())

# print("Is prime :",is_prime(number))