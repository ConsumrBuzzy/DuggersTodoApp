from todoItem import TodoItem
from todoListManager import TodoListManager

def cmd_list():
    print("Available commands:")
    print("  new       - add a new task")
    print("  list      - list tasks (optionally full)")
    print("  edit      - edit a task")
    print("  complete  - mark a task complete")
            print("  start     - start a task")
            print("  delete    - delete a task")
            print("  save      - save to todoList.json")
            print("  load      - load from todoList.json")
            print("  quit      - exit the program")

# Main Function
def main():
    todoListManager = TodoListManager()

    print("Dugger's TODO App")
    print("Type 'help' to see commands.")
    while True:
        user_input = input("Command> ").strip().lower()
        if user_input in ('q', 'quit', 'exit'):
            break
        elif user_input in ('help', 'h'):
            
        elif user_input == 'list':
            todoListManager.printTodoList()
        elif user_input == 'new':
            task_name = input("Enter a task name: ").strip()
            if task_name:
                todoListManager.addTodo(task_name)
                print(f"Added: {task_name}")
            else:
                print("Task name cannot be empty.")
        elif user_input == 'edit':
            task_name = input("Enter a task name to edit: ").strip()
            todoListManager.editTodo(task_name)
        elif user_input == 'complete':
            task_name = input("Enter a task name to complete: ").strip()
            todoListManager.completeTodo(task_name)
        elif user_input == 'start':
            task_name = input("Enter a task name to start: ").strip()
            todoListManager.startTodo(task_name)
        elif user_input == 'delete':
            task_name = input("Enter a task name to delete: ").strip()
            todoListManager.deleteTodo(task_name)
        elif user_input == 'save':
            todoListManager.saveTodoList("todoList.json")
            print("Saved to todoList.json")
        elif user_input == 'load':
            todoListManager.loadTodoList("todoList.json")
            print("Loaded from todoList.json")
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()