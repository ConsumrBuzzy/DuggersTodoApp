from todoItem import TodoItem
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
        if not self.todoList.__contains__(todoItem):
            self.todoList.append(todoItem)
        else:
            print("Todo already exists")
    # Remove Todo
    def remove(self, todoItem):
        if todoItem in self.todoList:
            for todo in self.todoList:
                if todo == todoItem:
                    self.todoList.remove(todoItem)

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
        temp_list = []
        for todo in self.todoList:
            # Convert datetime objects to string format
            if todo.createdAt is not None:
                todo.createdAt = todo.createdAt.strftime("%Y-%m-%d %H:%M:%S")
            if todo.completedAt is not None:
                todo.completedAt = todo.completedAt.strftime("%Y-%m-%d %H:%M:%S")
            if todo.startedAt is not None:
                todo.startedAt = todo.startedAt.strftime("%Y-%m-%d %H:%M:%S")

            # Append the dictionary representation to the temporary list
            temp_list.append(todo.__dict__)
        
        # Dump the entire list of dictionaries to the file
        with open(filename, "w") as file:
            json.dump(temp_list, file, indent=4)
        
    # Load Todo List
    def loadTodoList(self,filename):
        with open(filename, "r") as file:
            for todo in json.load(file):
                self.todoList.append(TodoItem(todo['taskName'], todo['isCompleted'], todo['taskPriority'], todo['taskDifficulty'], todo['taskDuration'], todo['taskCategory'], todo['taskDescription'], todo['estimatedDuration'], todo['completedAt'], todo['createdAt'], todo['startedAt']))
                if todo['createdAt'] is not None:
                    todo['createdAt'] = datetime.strptime(todo['createdAt'], "%Y-%m-%d %H:%M:%S")
                if todo['completedAt'] is not None:
                    todo['completedAt'] = datetime.strptime(todo['completedAt'], "%Y-%m-%d %H:%M:%S")
                if todo['startedAt'] is not None:
                    todo['startedAt'] = datetime.strptime(todo['startedAt'], "%Y-%m-%d %H:%M:%S")
        file.close()
    
    def getTodo(self, todoItem):
        for todo in self.todoList:
            if todo == todoItem:
                return todo