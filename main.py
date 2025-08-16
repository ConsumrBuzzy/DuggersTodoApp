from datetime import datetime
from todoItem import TodoItem

# Main Function
def main():
    todo_list = []
    print("Hello World")
    while True:
        user_input = input("Enter a task (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        todo_list.append(TodoItem(user_input, False, 0, 0, 0, "", "", 0))
        print(todo_list[-1])

# Entry Point
if __name__ == "__main__":
    main()