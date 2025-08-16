from datetime import datetime
from todoItem import TodoItem

# Main Function
def main():
    todo_list = []
    print("Hello World")
    while True:
        user_input = input("Enter 'new' to add a new task, 'q' to quit, 'print' to print the list): ")
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'print' or user_input.lower() == 'p':
            for todo in todo_list:
                print(str(todo_list.index(todo)+1) + ": " + todo.taskName )
                user_input = input("Enter the number corresponding to a task to select it: ")
                if user_input.isdigit():
                    selectedTodo = todo_list[int(user_input)-1]
                    user_input = input("Enter 'edit' to edit the task, 'complete' to complete the task, 'start' to start the task, 'quit' to quit, 'print' to print the task, 'delete' to delete the task: ")
                    if user_input.lower() == 'edit' or user_input.lower() == 'e':
                        selectedTodo.editTask()
                    elif user_input.lower() == 'complete' or user_input.lower() == 'c':
                        selectedTodo.completeTask()
                    elif user_input.lower() == 'start' or user_input.lower() == 's':
                        selectedTodo.startTask()
                    elif user_input.lower() == 'quit' or user_input.lower() == 'q':
                        break
                    elif user_input.lower() == 'print' or user_input.lower() == 'p':
                        print(selectedTodo)
                    elif user_input.lower() == 'delete' or user_input.lower() == 'd':
                        todo_list.remove(selectedTodo)
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
        elif user_input.lower() == 'new' or user_input.lower() == 'n':
            todo_list.append(TodoItem(False, 0, 0, 0, "", "", 0))
            print(todo_list[-1])
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()