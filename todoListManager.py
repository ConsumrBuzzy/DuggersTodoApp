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
        userAsk = input("'(f)ull Task Info? (Otherwise only Name of Tasks.)").lower()
        if userAsk == 'full' or userAsk == 'f':
            print(self.todoList.printTodoList(full=True))
        else:
            print(self.todoList.printTodoList(full=False))

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

    def menu(self):
        while True:
            user_input = input("Enter 'new' to add a new task, 'q' to quit, 'list' to print the list, 'save' to save the list, 'load' to load the list: ")
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'list' or user_input.lower() == 'l':
                self.printTodoList()
            elif user_input.lower() == 'new' or user_input.lower() == 'n':
                self.newTodo()
            elif user_input.lower() == 'save' or user_input.lower() == 's':
                self.saveTodoList("todoList.json")
            elif user_input.lower() == 'load' or user_input.lower() == 'l':
                self.loadTodoList("todoList.json")
            else:
                print("Invalid input")