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
        self.todoList.append(todoItem)
    # Remove Todo
    def remove(self, todoItem):
        if todoItem in self.todoList:
            for todo in self.todoList:
                if todo == todoItem:
                    self.todoList.remove(todoItem)

    # Print Todo List
    def printTodoList(self):
        for todo in self.todoList:
            print(str(self.todoList.index(todo)+1) + ": " + todo.taskName)
        user_input = input("Enter the number corresponding to a task to select it: ")
        if user_input.isdigit():
            selectedTodo = self.todoList[int(user_input)-1]
            user_input = input("Enter 'edit' to edit the task, 'complete' to complete the task, 'start' to start the task, 'quit' to quit, 'print' to print the task, 'delete' to delete the task: ")
            if user_input.lower() == 'edit' or user_input.lower() == 'e':
                selectedTodo.editTask()
            elif user_input.lower() == 'complete' or user_input.lower() == 'c':
                selectedTodo.completeTask()
            elif user_input.lower() == 'start' or user_input.lower() == 's':
                selectedTodo.startTask()
            elif user_input.lower() == 'quit' or user_input.lower() == 'q':
                return
            elif user_input.lower() == 'print' or user_input.lower() == 'p':
                print(selectedTodo)
            elif user_input.lower() == 'delete' or user_input.lower() == 'd':
                self.remove(selectedTodo)
        else:
            print("Invalid input")

    # String Representation
    def __str__(self):
        return "\n".join([str(todo) for todo in self.todoList])
    
    # Save Todo List
    def saveTodoList(self):
        filename = "todoList.json"
        temp_list = []
        for todo in self.todoList:
            # Convert datetime objects to string format
            if todo.createdAt is not None:
                todo.createdAt = todo.createdAt.isoformat()
            if todo.completedAt is not None:
                todo.completedAt = todo.completedAt.isoformat()
            if todo.startedAt is not None:
                todo.startedAt = todo.startedAt.isoformat()

            # Append the dictionary representation to the temporary list
            temp_list.append(todo.__dict__)
        
        # Dump the entire list of dictionaries to the file
        with open(filename, "w") as file:
            json.dump(temp_list, file, indent=4)
        
    # Load Todo List
    def loadTodoList(self):
        filename = "todoList.json"
        with open(filename, "r") as file:
            for todo in json.load(file):
                if todo['createdAt'] is not None:
                    todo['createdAt'] = datetime.fromisoformat(todo['createdAt'])
                if todo['completedAt'] is not None:
                    todo['completedAt'] = datetime.fromisoformat(todo['completedAt'])
                if todo['startedAt'] is not None:
                    todo['startedAt'] = datetime.fromisoformat(todo['startedAt'])
                self.todoList.append(TodoItem(**todo))
        file.close()
    