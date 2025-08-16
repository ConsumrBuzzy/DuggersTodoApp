from datetime import datetime
from todoItem import TodoItem
from todoList import TodoList

# Main Function
def main():
    todoList = TodoList()

    print("Hello World")
    while True:
        user_input = input("Enter 'new' to add a new task, 'q' to quit, 'print' to print the list): ")
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'print' or user_input.lower() == 'p':
            todoList.printTodoList()
        elif user_input.lower() == 'new' or user_input.lower() == 'n':
            todoList.addTodo(TodoItem())
            print(todoList.todoList[-1])
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()