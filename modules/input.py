def user_input():
    option = input("Select an option 1, 2, 3, 4, 5, 6, 7 or (Q)uit: ")
    return option

def task_description():
    description = input("Enter task description to search for: ")
    return description

def task_time():
    time = int(input("Enter task duration: "))
    return time


def add_task_description():
    description = input("Enter description: ")
    return description

def add_time_taken():
    time_taken = int(input("Enter time taken: "))
    return time_taken