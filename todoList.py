from todoItem import TodoItem
from datetime import datetime
import json

class TodoList:
    # Todo List
    todoList = []
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
    def printTodoList(self, full=False):
        if full:
            return "\n".join([todo.printFull() for todo in self.todoList])
        else:
            return "\n".join([todo.taskName for todo in self.todoList])

    # String Representation
    def __str__(self):
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
        self.todoList = []
        with open(filename, "r") as file:
            for todo in json.load(file):
                createdAt = datetime.strptime(todo['createdAt'], "%Y-%m-%d %H:%M:%S") if todo.get('createdAt') else None
                completedAt = datetime.strptime(todo['completedAt'], "%Y-%m-%d %H:%M:%S") if todo.get('completedAt') else None
                startedAt = datetime.strptime(todo['startedAt'], "%Y-%m-%d %H:%M:%S") if todo.get('startedAt') else None
                item = TodoItem(
                    taskName=todo['taskName'],
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
                self.todoList.append(item)
    
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

    def completeTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.completeTask()
        else:
            print("Todo not found")

    def startTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.startTask()
        else:
            print("Todo not found")

    def deleteTodo(self, todoItem):
        todo = self.getTodo(todoItem)
        if todo:
            todo.deleteTask()
            self.remove(todo)
        else:
            print("Todo not found")