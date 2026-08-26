# to do List

TodoList = []


def addTask(task):
    task = {"description": task, "completed": False}
    TodoList.append(task)

    print("\nTask added successfully!")

def delTask(task):
    for t in TodoList:
        if t.get("description") == task:
            TodoList.remove(t)
            print("\nTask removed successfully!")
            return
        
    print("Task not found in the list.")

def completeTask(task):
    for t in TodoList:
        if t.get ("description") == task:
            t['completed'] = True
            print("\n Task marked as completed!")
            return
        
    print("Task not found in the list.")

def viewTask():
    print("\nTasks :- ")
    if len(TodoList) == 0:
        print("No tasks in the list.")
    else:
        for i in TodoList:
            print(".",i["description"], " ✔️ " if i["completed"] else " ❌ ")
        print("\n")

def menu():
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Complete Task")
    print("5. Exit")



def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            addTask(task)
        elif choice == 2:
            task = input("Enter the task to delete: ")
            delTask(task)
        elif choice == 3:
            viewTask()
        elif choice == 4:
            completeTask(input("Enter the task to mark as completed: "))
        elif choice == 5:
                    print("Exiting the program...")
                    break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()