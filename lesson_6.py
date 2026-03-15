# import os
# import string
# from collections import Counter

# # ===============================
# # 1. ZERO CHECK DECORATOR
# # ===============================

# def zero_check(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "Denominator can't be zero"
#         return func(a, b)
#     return wrapper


# @zero_check
# def div(a, b):
#     return a / b


# # ===============================
# # 2. EMPLOYEE RECORDS MANAGER
# # ===============================

# FILE_NAME = "employees.txt"


# def add_employee():
#     emp_id = input("Enter employee ID: ")
#     name = input("Enter name: ")
#     position = input("Enter position: ")
#     salary = input("Enter salary: ")

#     record = f"{emp_id},{name},{position},{salary}\n"

#     with open(FILE_NAME, "a") as f:
#         f.write(record)

#     print("Employee added successfully.")


# def view_employees():
#     if not os.path.exists(FILE_NAME):
#         print("No records found.")
#         return

#     with open(FILE_NAME, "r") as f:
#         print("\nEmployee Records:")
#         for line in f:
#             emp_id, name, position, salary = line.strip().split(",")
#             print(f"ID: {emp_id} | Name: {name} | Position: {position} | Salary: {salary}")


# def employee_manager():

#     while True:
#         print("\nEmployee Records Manager")
#         print("1. Add Employee")
#         print("2. View Employees")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_employee()

#         elif choice == "2":
#             view_employees()

#         elif choice == "3":
#             print("Exiting program.")
#             break

#         else:
#             print("Invalid choice.")


# # ===============================
# # 3. WORD FREQUENCY COUNTER
# # ===============================

# def word_counter():

#     file_name = "sample.txt"

#     if not os.path.exists(file_name):
#         print("sample.txt does not exist.")
#         text = input("Please type a paragraph:\n")

#         with open(file_name, "w") as f:
#             f.write(text)

#     with open(file_name, "r") as f:
#         text = f.read()

#     text = text.lower()
#     text = text.translate(str.maketrans("", "", string.punctuation))

#     words = text.split()

#     word_counts = Counter(words)

#     total_words = len(words)
#     top_words = word_counts.most_common(5)

#     print(f"\nTotal words: {total_words}")
#     print("Top 5 most common words:")

#     for word, count in top_words:
#         print(f"{word} - {count} times")

#     with open("word_count_report.txt", "w") as report:
#         report.write("Word Count Report\n")
#         report.write(f"Total Words: {total_words}\n")
#         report.write("Top 5 Words:\n")

#         for word, count in top_words:
#             report.write(f"{word} - {count}\n")

#     print("Report saved to word_count_report.txt")


# # ===============================
# # MAIN PROGRAM
# # ===============================

# if __name__ == "__main__":

#     print("\nDivision Test")
#     print(div(10, 2))
#     print(div(10, 0))

#     employee_manager()

#     word_counter()