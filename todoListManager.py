from todoList import TodoList
from todoItem import TodoItem

class TodoListManager:
    
    def __init__(self):
        self.todoList = TodoList()
    
    def addTodo(self, todoItem):
        self.todoList.addTodo(todoItem)
    
    def removeTodo(self, todoItem):
        self.todoList.remove(todoItem)
    
    def saveTodoList(self, filename):
        self.todoList.saveTodoList(filename)
    
    def loadTodoList(self, filename):
        self.todoList.loadTodoList(filename)
    
    def printTodoList(self):
        userAsk = input("(f)ull task info? (Otherwise only names): ").strip().lower()
        full = userAsk in ('full', 'f', 'yes', 'y')
        print(self.todoList.printTodoList(full=full))

    def editTodo(self, todoItem):
        self.todoList.editTodo(todoItem)
    
    def completeTodo(self, todoItem):
        self.todoList.completeTodo(todoItem)
    
    def startTodo(self, todoItem):
        self.todoList.startTodo(todoItem)
    
    def deleteTodo(self, todoItem):
        self.todoList.deleteTodo(todoItem)
    
    def getTodo(self, todoItem):
        return self.todoList.getTodo(todoItem)
    
    def newTodo(self):
        taskName = input("Enter a task name: ")
        self.todoList.addTodo(TodoItem(taskName))