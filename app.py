import pdb

from modules.output import *
from modules.task_list import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    # pdb.set_trace()
    option = user_input()
    # user_input()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        # description = input("Enter task description to search for: ")
        description = task_description()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        # time = int(input("Enter task duration: "))
        time = task_time()
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        # description = input("Enter task description to search for: ")
        description = task_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        # description = input("Enter description: ")
        description = add_task_description()
        # time_taken = int(input("Enter time taken: "))
        time_taken = add_time_taken()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
