

class take_task:
    def __init__(self,task_id, title, description, date, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.date = date
        self.status = status

        

    def __str__(self):
        task_info = [self.id, self.title, self.description, self.date, self.status]
        answer = ", ".join(task_info)
        return answer

        

menyu = """Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit"""


class Aplication:
    while 1:
        print(menyu)
        number = int(input())
        if number == 1:
            task_id = int(input("Enter Task ID: "))
            task_title = input("Enter Title: ")
            task_des = input("Enter Description: ")
            task_date = input("Enter Due Date (YYYY-MM-DD): ")
            task_status = input("Enter Status (Pending/In Progress/Completed):")

            if task_date == "":
                task_date = "Not Given !"

            new_task = take_task(task_id, task_title, task_des, task_date, task_status)
            



            print("Task added successfully !")
        elif number == 2:
            pass
        elif number == 3:
            pass
        elif number == 4:
            pass
        elif number == 5:
            pass
        elif number == 6:
            pass
        elif number == 7:
            pass
        elif number == 8:
            pass
        
        else:
            print("Pleaase choose from the number from menyu !")
