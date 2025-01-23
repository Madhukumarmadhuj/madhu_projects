tasks=["madhu","kumar","jambu"]
def show_menu():
    print("to do list in menu")
    print("1.view the task")
    print("2.add task")
    print("3.remove task")
    print("4.reminder")
    print("5.exit")
def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        index=1
        for task in tasks:
            print(f"{index}.{task}")
            index+=1

def add_task():
    task=input("enter a adding task name")
    tasks.append(task)
    print(f"{task} added sucessfully")


def remov_task():
    if not tasks:
        print("no tasks should be present")
        return
    view_tasks()
    while True:
        try:
            task_no=int(input("enter a task name NUMBER FOR DELETING"))
            if task_no<=len(tasks):
                remove=tasks.pop(task_no-1)
                print(f"{remove} remove this tasks")
                break
            else:
                print("enter a correct number")

        except value_error:
            print("enter a valid number")


while True:
    show_menu()
    choices=int(input("enter 1--5"))
    if choices==1:
        view_tasks()
    elif choices==2:
        add_task()
    elif choices==3:
        remov_task()
    elif choices==4:
        remind()
    elif choices==5:
        print("exiting list app good bye")
        break
    else:
        print("enter a correct choice")

