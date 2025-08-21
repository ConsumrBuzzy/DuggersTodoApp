from todoItem import TodoItem
from todoListManager import TodoListManager as manager

def show_help(todoListManager):
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

# Add a new task
def handle_new(todoListManager):
    task_name = input("Enter a task name: ").strip()
    if task_name:
        todoListManager.addTodo(task_name)
        print(f"Added: {task_name}")
    else:
        print("Task name cannot be empty.")

# Edit a task
def handle_edit(todoListManager):
    task_name = input("Enter a task name to edit: ").strip()
    todoListManager.editTodo(task_name)

# Mark a task as complete
def handle_complete(todoListManager):
    task_name = input("Enter a task name to complete: ").strip()
    todoListManager.completeTodo(task_name)

# Start a task
def handle_start(todoListManager):
    task_name = input("Enter a task name to start: ").strip()
    todoListManager.startTodo(task_name)

# Delete a task
def handle_delete(todoListManager):
    task_name = input("Enter a task name to delete: ").strip()
    todoListManager.deleteTodo(task_name)

# Save the todo list to a file
def handle_save(todoListManager):
    todoListManager.saveTodoList("todoList.json")
    print("Saved to todoList.json")

# Load the todo list from a file
def handle_load(todoListManager):
    if todoListManager.loadTodoList("todoList.json"):
        print("Loaded from todoList.json")
    else:
        print("Load failed.")

# Quit the program
def handle_quit(todoListManager):
    todoListManager.saveTodoList("todoList.json")
    print("Goodbye!")
    exit()

# Main Function
def main():
    todoListManager = manager()

    print("Dugger's TODO App")
    print("Type 'help' to see commands.")

    # Command Dictionary
    COMMANDS = {
        'help': lambda: show_help(todoListManager),
        'list': lambda: todoListManager.printTodoList(),
        'new': lambda: handle_new(todoListManager),
        'edit': lambda: handle_edit(todoListManager),
        'complete': lambda: handle_complete(todoListManager),
        'start': lambda: handle_start(todoListManager),
        'delete': lambda: handle_delete(todoListManager),
        'save': lambda: handle_save(todoListManager),
        'load': lambda: handle_load(todoListManager),
        'quit': lambda: handle_quit(todoListManager),
    }

    # Main Loop
    while True:
        user_input = input("Command> ").strip().lower()
        if user_input in COMMANDS:
            COMMANDS[user_input]()
        else:
            print("Invalid input")

# Entry Point
if __name__ == "__main__":
    main()