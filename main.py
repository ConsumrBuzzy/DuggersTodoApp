from todoItem import TodoItem
from todoListManager import TodoListManager

# Main Function
def main():
    todoListManager = TodoListManager()

    print("Hello World")
    while True:
        user_input = input("Enter 'new' to add a new task, 'q' to quit, 'list' to print the list, 'save' to save the list, 'load' to load the list: ")
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'list' or user_input.lower() == 'l':
            todoListManager.printTodoList()
        elif user_input.lower() == 'new' or user_input.lower() == 'n':
            task_name = input("Enter a task name: ")
            todoListManager.addTodo(task_name)
            print(todoListManager.getTodo(task_name))
        elif user_input.lower() == 'save' or user_input.lower() == 's':
            todoListManager.saveTodoList("todoList.json")
        elif user_input.lower() == 'load' or user_input.lower() == 'l':
            todoListManager.loadTodoList("todoList.json")
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()