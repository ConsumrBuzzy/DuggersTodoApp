from todoItem import TodoItem
from todoList import TodoList

# Main Function
def main():
    todoList = TodoList()

    print("Hello World")
    while True:
        user_input = input("Enter 'new' to add a new task, 'q' to quit, 'list' to print the list, 'save' to save the list, 'load' to load the list: ")
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'list' or user_input.lower() == 'l':
            todoList.printTodoList()
        elif user_input.lower() == 'new' or user_input.lower() == 'n':
            task_name = input("Enter a task name: ")
            todoList.addTodo(TodoItem(task_name))
            print(todoList.todoList[-1])
        elif user_input.lower() == 'save' or user_input.lower() == 's':
            todoList.saveTodoList()
        elif user_input.lower() == 'load' or user_input.lower() == 'l':
            todoList.loadTodoList()
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()