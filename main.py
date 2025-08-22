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
    print("  help      - show this help message")
    print("  set       - one-shot edit: change a single field (name|priority|difficulty|duration|category|description)")
    print("  e.g. set <task name> <field> <value>")
    print("  e.g. set <task name> name <new name>")
    print("  e.g. set <task name> priority <new priority>")
    print("  e.g. set <task name> difficulty <new difficulty>")
    print("  e.g. set <task name> duration <new duration>")
    print("  e.g. set <task name> category <new category>")
    print("  e.g. set <task name> description <new description>")
    print("  e.g. set <task name> estimatedDuration <new estimated duration>")
    print("  stats     - show totals and averages across tasks")

# Add a new task
def handle_new(todo_list: TodoList):
    task_name = input("Enter a task name: ").strip()
    if task_name:
        if todo_list.addTodo(task_name):
            print(f"Added: {task_name}")
            # Auto-save after mutation
            todo_list.saveTodoList("todoList.json")
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
        choice = input("Edit (name|priority|difficulty|duration|category|description|estimatedDuration|quit): ").strip().lower()
        if choice in ('quit', 'q'):
            break
        elif choice in ('name', 'n'):
            new_val = input("New name: ").strip()
            if new_val:
                todo.set_name(new_val)
                print("Name updated.")
                todo_list.saveTodoList("todoList.json")
            else:
                print("Name cannot be empty.")
        elif choice in ('priority', 'p'):
            raw = input("New priority (integer): ").strip()
            try:
                todo.set_priority(int(raw))
                print("Priority updated.")
                todo_list.saveTodoList("todoList.json")
            except ValueError:
                print("Invalid number.")
        elif choice in ('difficulty', 'd'):
            raw = input("New difficulty (integer): ").strip()
            try:
                todo.set_difficulty(int(raw))
                print("Difficulty updated.")
                todo_list.saveTodoList("todoList.json")
            except ValueError:
                print("Invalid number.")
        elif choice in ('duration', 'dur'):
            raw = input("New duration (integer minutes): ").strip()
            try:
                todo.set_duration(int(raw))
                print("Duration updated.")
                todo_list.saveTodoList("todoList.json")
            except ValueError:
                print("Invalid number.")
        elif choice in ('category', 'cat'):
            todo.set_category(input("New category: "))
            print("Category updated.")
            todo_list.saveTodoList("todoList.json")
        elif choice in ('description', 'desc'):
            todo.set_description(input("New description: "))
            print("Description updated.")
            todo_list.saveTodoList("todoList.json")
        elif choice in ('estimatedduration', 'estimated', 'eta', 'ed'):
            raw = input("New estimated duration (integer minutes): ").strip()
            try:
                todo.set_estimated_duration(int(raw))
                print("Estimated duration updated.")
                todo_list.saveTodoList("todoList.json")
            except ValueError:
                print("Invalid number.")
        else:
            print("Invalid choice.")

# One-shot setter (non-interactive single field update)
def handle_set(todo_list: TodoList):
    name = input("Task name: ").strip()
    if not name:
        print("Task name cannot be empty.")
        return
    todo = todo_list.getTodoByName(name)
    if not todo:
        print("Todo not found.")
        return
    field = input("Field (name|priority|difficulty|duration|category|description|estimatedDuration): ").strip().lower()
    if field in ("name", "n"):
        new_val = input("New name: ").strip()
        if new_val:
            todo.set_name(new_val)
            print("Name updated.")
            todo_list.saveTodoList("todoList.json")
        else:
            print("Name cannot be empty.")
    elif field in ("priority", "p"):
        raw = input("New priority (integer): ").strip()
        try:
            todo.set_priority(int(raw))
            print("Priority updated.")
            todo_list.saveTodoList("todoList.json")
        except ValueError:
            print("Invalid number.")
    elif field in ("difficulty", "d"):
        raw = input("New difficulty (integer): ").strip()
        try:
            todo.set_difficulty(int(raw))
            print("Difficulty updated.")
            todo_list.saveTodoList("todoList.json")
        except ValueError:
            print("Invalid number.")
    elif field in ("duration", "dur"):
        raw = input("New duration (integer minutes): ").strip()
        try:
            todo.set_duration(int(raw))
            print("Duration updated.")
            todo_list.saveTodoList("todoList.json")
        except ValueError:
            print("Invalid number.")
    elif field in ("category", "cat"):
        todo.set_category(input("New category: "))
        print("Category updated.")
        todo_list.saveTodoList("todoList.json")
        
    elif field in ("description", "desc"):
        todo.set_description(input("New description: "))
        print("Description updated.")
        todo_list.saveTodoList("todoList.json")
    elif field in ("estimatedduration", "estimated", "eta", "ed"):
        raw = input("New estimated duration (integer minutes): ").strip()
        try:
            todo.set_estimated_duration(int(raw))
            print("Estimated duration updated.")
            todo_list.saveTodoList("todoList.json")
        except ValueError:
            print("Invalid number.")
    else:
        print("Unknown field.")

# Mark a task as complete
def handle_complete(todo_list: TodoList):
    task_name = input("Enter a task name to complete: ").strip()
    if todo_list.completeTodo(task_name):
        print("Marked complete.")
        todo_list.saveTodoList("todoList.json")
    else:
        print("Todo not found.")

# Start a task
def handle_start(todo_list: TodoList):
    task_name = input("Enter a task name to start: ").strip()
    if todo_list.startTodo(task_name):
        print("Started.")
        todo_list.saveTodoList("todoList.json")
    else:
        print("Todo not found.")

# Delete a task
def handle_delete(todo_list: TodoList):
    task_name = input("Enter a task name to delete: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return
    todo = todo_list.getTodoByName(task_name)
    if not todo:
        print("Todo not found.")
        return
    confirm = input(f"Are you sure you want to delete '{todo.taskName}'? (y/N): ").strip().lower()
    if confirm in ("y", "yes"):
        if todo_list.deleteTodo(todo):
            print("Deleted.")
            todo_list.saveTodoList("todoList.json")
        else:
            print("Delete failed.")
    else:
        print("Delete cancelled.")

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

# Show basic statistics
def handle_stats(todo_list: TodoList):
    items = list(todo_list.todoList)
    total = len(items)
    completed = sum(1 for t in items if t.isCompleted)
    started = sum(1 for t in items if t.startedAt is not None)
    # Averages (avoid divide by zero)
    if total:
        avg_prio = sum(t.taskPriority for t in items) / total
        avg_diff = sum(t.taskDifficulty for t in items) / total
    else:
        avg_prio = 0.0
        avg_diff = 0.0
    total_est = sum((t.estimatedDuration or 0) for t in items)
    total_dur = sum((t.taskDuration or 0) for t in items)
    print("Stats:")
    print(f"  Total tasks: {total}")
    print(f"  Completed:   {completed}")
    print(f"  Started:     {started}")
    print(f"  Avg priority:   {avg_prio:.2f}")
    print(f"  Avg difficulty: {avg_diff:.2f}")
    print(f"  Total estimated minutes: {total_est}")
    print(f"  Total actual minutes:    {total_dur}")

# List tasks (prompt for full in CLI)
def handle_list(todo_list: TodoList):
    userAsk = input("(f)ull task info? (Otherwise only names): ").strip().lower()
    full = userAsk in ("full", "f", "yes", "y")

    # Optional sorting
    sort_key = input("Sort by (name|priority|difficulty|duration|estimated|none): ").strip().lower()
    valid_sorts = {"name", "priority", "difficulty", "duration", "estimated", "none", ""}
    if sort_key not in valid_sorts:
        print("Unknown sort key. Showing unsorted.")
        sort_key = "none"

    items = list(todo_list.todoList)
    if sort_key == "name":
        items.sort(key=lambda t: (t.taskName or "").lower())
    elif sort_key == "priority":
        items.sort(key=lambda t: t.taskPriority)
    elif sort_key == "difficulty":
        items.sort(key=lambda t: t.taskDifficulty)
    elif sort_key == "duration":
        items.sort(key=lambda t: t.taskDuration)
    elif sort_key == "estimated":
        items.sort(key=lambda t: t.estimatedDuration)

    lines = []
    for idx, t in enumerate(items, start=1):
        mark = "[x]" if t.isCompleted else "[ ]"
        if full:
            lines.append(
                f"{idx:>2}. {mark} {t.taskName} | prio={t.taskPriority} diff={t.taskDifficulty} dur={t.taskDuration}m est={t.estimatedDuration}m"
            )
        else:
            lines.append(f"{idx:>2}. {mark} {t.taskName}")
    print("\n".join(lines) if lines else "(no tasks)")

# Quit the program
def handle_quit(todo_list: TodoList):
    todo_list.saveTodoList("todoList.json")
    print("Goodbye!")
    exit()

# Main Function
def main():
    todo_list = TodoList()
    # Auto-load on startup
    if todo_list.loadTodoList("todoList.json"):
        print("Loaded existing todo list from todoList.json")
    else:
        print("Starting with an empty todo list.")

    print("Dugger's TODO App")
    print("Type 'help' to see commands.")

    # Command Dictionary
    COMMANDS = {
        'help': lambda: show_help(todo_list),
        'list': lambda: handle_list(todo_list),
        'new': lambda: handle_new(todo_list),
        'edit': lambda: handle_edit(todo_list),
        'set': lambda: handle_set(todo_list),
        'complete': lambda: handle_complete(todo_list),
        'start': lambda: handle_start(todo_list),
        'delete': lambda: handle_delete(todo_list),
        'save': lambda: handle_save(todo_list),
        'load': lambda: handle_load(todo_list),
        'stats': lambda: handle_stats(todo_list),
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