from todoItem import TodoItem
from datetime import datetime
import json

class TodoList:
    

    # Constructor
    def __init__(self):
        self.todoList = []
    # Add Todo
    def addTodo(self, todoItem):
        # Accept either a TodoItem instance or a task name string
        item = todoItem if isinstance(todoItem, TodoItem) else TodoItem(str(todoItem))
        # Ensure no duplicates by taskName
        if all(existing.taskName != item.taskName for existing in self.todoList):
            self.todoList.append(item)
        else:
            print("Todo already exists")
    
    # Remove Todo
    def remove(self, todoItem):
        name = todoItem.taskName if isinstance(todoItem, TodoItem) else str(todoItem)
        self.todoList = [t for t in self.todoList if t.taskName != name]

    # Print Todo List
    def printTodoList(self, full: bool = False):
        if full:
            return "\n".join([todo.printFull() for todo in self.todoList])
        else:
            return "\n".join([todo.taskName for todo in self.todoList])
    
    # Save Todo List
    def saveTodoList(self,filename):
        serializable = []
        for t in self.todoList:
            serializable.append({
                'taskName': t.taskName,
                'isCompleted': t.isCompleted,
                'taskPriority': t.taskPriority,
                'taskDifficulty': t.taskDifficulty,
                'taskDuration': t.taskDuration,
                'taskCategory': t.taskCategory,
                'taskDescription': t.taskDescription,
                'estimatedDuration': t.estimatedDuration,
                'completedAt': t.completedAt.strftime("%Y-%m-%d %H:%M:%S") if t.completedAt else None,
                'createdAt': t.createdAt.strftime("%Y-%m-%d %H:%M:%S") if t.createdAt else None,
                'startedAt': t.startedAt.strftime("%Y-%m-%d %H:%M:%S") if t.startedAt else None,
            })
        with open(filename, "w") as file:
            json.dump(serializable, file, indent=4)
        
    # Load Todo List
    def loadTodoList(self,filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No saved todo list found.")
            return False
        except json.JSONDecodeError:
            print("Could not read todo list (invalid JSON).")
            return False

        new_list = []
        for todo in data:
            raw_created = todo.get('createdAt')
            raw_completed = todo.get('completedAt')
            raw_started = todo.get('startedAt')
            try:
                createdAt = datetime.strptime(raw_created, "%Y-%m-%d %H:%M:%S") if raw_created else None
            except Exception:
                createdAt = None
            try:
                completedAt = datetime.strptime(raw_completed, "%Y-%m-%d %H:%M:%S") if raw_completed else None
            except Exception:
                completedAt = None
            try:
                startedAt = datetime.strptime(raw_started, "%Y-%m-%d %H:%M:%S") if raw_started else None
            except Exception:
                startedAt = None

            item = TodoItem(
                taskName=todo.get('taskName', ''),
                isCompleted=todo.get('isCompleted', False),
                taskPriority=todo.get('taskPriority', 0),
                taskDifficulty=todo.get('taskDifficulty', 0),
                taskDuration=todo.get('taskDuration', 0),
                taskCategory=todo.get('taskCategory', ""),
                taskDescription=todo.get('taskDescription', ""),
                estimatedDuration=todo.get('estimatedDuration', 0),
                completedAt=completedAt,
                createdAt=createdAt,
                startedAt=startedAt,
            )
            new_list.append(item)

        self.todoList = new_list
        return True
    
    # Get Todo
    def getTodo(self, todoItem):
        for todo in self.todoList:
            if todo == todoItem:
                return todo
        return None

    # Convenience operations by name
    def editTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.editTask()
        else:
            print("Todo not found")

    # Complete Todo
    def completeTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.completeTask()
        else:
            print("Todo not found")

    # Start Todo
    def startTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.startTask()
        else:
            print("Todo not found")

    # Delete Todo
    def deleteTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.deleteTask()
            self.remove(todo)
        else:
            print("Todo not found")
    
    # String Representation
    def __str__(self):
        return "\n".join([todo.taskName for todo in self.todoList])