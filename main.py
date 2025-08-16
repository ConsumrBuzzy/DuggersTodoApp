from datetime import datetime
from todoItem import TodoItem

# Main Function
def main():
    todo_list = []
    print("Hello World")
    while True:
        user_input = input("Enter 'new' to add a new task, 'q' to quit, 'print' to print the list): ")
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'print':
            for todo in todo_list:
                print(todo)
        elif user_input.lower() == 'new':
            todo_list.append(TodoItem(False, 0, 0, 0, "", "", 0))
            print(todo_list[-1])
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()