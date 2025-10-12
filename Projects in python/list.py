todo_list = [] 
def show_tasks():
    """Display all tasks in the to-do list."""
    if not todo_list:
        print("\nNo tasks available!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(index, " -> ", task)
def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter task: ")
    todo_list.append(task)
    print("Task ->", task, "is added")
def remove_task():
    """Remove a completed task from the to-do list."""
    show_tasks()
    if todo_list:
        task_no = int(input("\nEnter task number to remove: "))
        if 1 <= task_no <= len(todo_list):
            removed_task = todo_list.pop(task_no - 1)
            print("Task ->", removed_task, "is removed!")
        else:
            print("Invalid task number!")
    show_tasks()
def main():
    """Main function to run the to-do list program."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")
main()
