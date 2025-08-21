from todoItem import TodoItem
from todoList import TodoList

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
def handle_new(todo_list: TodoList):
    task_name = input("Enter a task name: ").strip()
    if task_name:
        if todo_list.addTodo(task_name):
            print(f"Added: {task_name}")
        else:
            print("Todo already exists.")
    else:
        print("Task name cannot be empty.")

# Edit a task (interactive, CLI only)
def handle_edit(todo_list: TodoList):
    task_name = input("Enter a task name to edit: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return
    todo = todo_list.getTodoByName(task_name)
    if not todo:
        print("Todo not found")
        return
    while True:
        choice = input("Edit (name|priority|difficulty|duration|category|description|quit): ").strip().lower()
        if choice in ('quit', 'q'):
            break
        elif choice in ('name', 'n'):
            new_val = input("New name: ").strip()
            if new_val:
                todo.set_name(new_val)
                print("Name updated.")
            else:
                print("Name cannot be empty.")
        elif choice in ('priority', 'p'):
            raw = input("New priority (integer): ").strip()
            try:
                todo.set_priority(int(raw))
                print("Priority updated.")
            except ValueError:
                print("Invalid number.")
        elif choice in ('difficulty', 'd'):
            raw = input("New difficulty (integer): ").strip()
            try:
                todo.set_difficulty(int(raw))
                print("Difficulty updated.")
            except ValueError:
                print("Invalid number.")
        elif choice in ('duration', 'dur'):
            raw = input("New duration (integer minutes): ").strip()
            try:
                todo.set_duration(int(raw))
                print("Duration updated.")
            except ValueError:
                print("Invalid number.")
        elif choice in ('category', 'cat'):
            todo.set_category(input("New category: "))
            print("Category updated.")
        elif choice in ('description', 'desc'):
            todo.set_description(input("New description: "))
            print("Description updated.")
        else:
            print("Invalid choice.")

# Mark a task as complete
def handle_complete(todo_list: TodoList):
    task_name = input("Enter a task name to complete: ").strip()
    if todo_list.completeTodo(task_name):
        print("Marked complete.")
    else:
        print("Todo not found.")

# Start a task
def handle_start(todo_list: TodoList):
    task_name = input("Enter a task name to start: ").strip()
    if todo_list.startTodo(task_name):
        print("Started.")
    else:
        print("Todo not found.")

# Delete a task
def handle_delete(todo_list: TodoList):
    task_name = input("Enter a task name to delete: ").strip()
    if todo_list.deleteTodo(task_name):
        print("Deleted.")
    else:
        print("Todo not found.")

# Save the todo list to a file
def handle_save(todo_list: TodoList):
    todo_list.saveTodoList("todoList.json")
    print("Saved to todoList.json")

# Load the todo list from a file
def handle_load(todo_list: TodoList):
    if todo_list.loadTodoList("todoList.json"):
        print("Loaded from todoList.json")
    else:
        print("Load failed.")

# List tasks (prompt for full in CLI)
def handle_list(todo_list: TodoList):
    userAsk = input("(f)ull task info? (Otherwise only names): ").strip().lower()
    full = userAsk in ("full", "f", "yes", "y")
    print(todo_list.printTodoList(full=full))

# Quit the program
def handle_quit(todo_list: TodoList):
    todo_list.saveTodoList("todoList.json")
    print("Goodbye!")
    exit()

# Main Function
def main():
    todo_list = TodoList()

    print("Dugger's TODO App")
    print("Type 'help' to see commands.")

    # Command Dictionary
    COMMANDS = {
        'help': lambda: show_help(todo_list),
        'list': lambda: handle_list(todo_list),
        'new': lambda: handle_new(todo_list),
        'edit': lambda: handle_edit(todo_list),
        'complete': lambda: handle_complete(todo_list),
        'start': lambda: handle_start(todo_list),
        'delete': lambda: handle_delete(todo_list),
        'save': lambda: handle_save(todo_list),
        'load': lambda: handle_load(todo_list),
        'quit': lambda: handle_quit(todo_list),
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