from datetime import datetime

class TodoItem:    
    # Constructor
    def __init__(self, taskName, isCompleted=False, taskPriority=0, taskDifficulty=0, taskDuration=0, taskCategory="", taskDescription="", estimatedDuration=0, completedAt=None, createdAt=None, startedAt=None):
        self.taskName = taskName
        self.isCompleted = isCompleted
        self.createdAt = createdAt if createdAt is not None else datetime.now()
        self.completedAt = completedAt
        self.startedAt = startedAt
        self.estimatedDuration = estimatedDuration
        self.taskDuration = taskDuration
        self.taskPriority = taskPriority
        self.taskDifficulty = taskDifficulty
        self.taskCategory = taskCategory
        self.taskDescription = taskDescription
        self.isDeleted = False

    def printName(self):
        return self.taskName

    def printFull(self):
        return f"Task Name: {self.taskName}\nTask Priority: {self.taskPriority}\nTask Difficulty: {self.taskDifficulty}\nTask Category: {self.taskCategory}\nTask Description: {self.taskDescription}\nTask Duration: {self.taskDuration}\nTask Completion Status: {self.isCompleted}\nTask Completion Time: {self.completedAt}\nTask Creation Time: {self.createdAt}\nTask Estimated Duration: {self.estimatedDuration}\nTask Start Time: {self.startedAt}"

    def startTask(self):
        self.startedAt = datetime.now()
    
    def setTaskName(self):
        taskName = input("Enter a task name: ")
        return taskName

    def completeTask(self):
        self.isCompleted = True
        self.completedAt = datetime.now()
    
    def editTask(self):
        while True:
            user_input = input("Enter 'name' to edit the task name, 'priority' to edit the task priority, 'difficulty' to edit the task difficulty, 'duration' to edit the task duration, 'category' to edit the task category, 'description' to edit the task description, 'quit' to quit: ")
            if user_input.lower() == 'quit' or user_input.lower() == 'q':
                break
            elif user_input.lower() == 'name' or user_input.lower() == 'n':
                self.taskName = self.setTaskName()
            elif user_input.lower() == 'priority' or user_input.lower() == 'p':
                raw = input("Enter a task priority (integer): ")
                try:
                    self.taskPriority = int(raw)
                except ValueError:
                    print("Invalid number. Priority unchanged.")
            elif user_input.lower() == 'difficulty' or user_input.lower() == 'd':
                raw = input("Enter a task difficulty (integer): ")
                try:
                    self.taskDifficulty = int(raw)
                except ValueError:
                    print("Invalid number. Difficulty unchanged.")
            elif user_input.lower() == 'duration' or user_input.lower() == 'dur':
                raw = input("Enter a task duration (integer minutes): ")
                try:
                    self.taskDuration = int(raw)
                except ValueError:
                    print("Invalid number. Duration unchanged.")
            elif user_input.lower() == 'category' or user_input.lower() == 'cat':
                self.taskCategory = input("Enter a task category: ")
            elif user_input.lower() == 'description' or user_input.lower() == 'desc':
                self.taskDescription = input("Enter a task description: ")
            else:
                print("Invalid input")
    
    def deleteTask(self):
        self.isDeleted = True

    def getTaskName(self):
        return self.taskName

    def getTaskPriority(self):
        return self.taskPriority

    def getTaskDifficulty(self):
        return self.taskDifficulty

    def getTaskCategory(self):
        return self.taskCategory

    def getTaskDescription(self):
        return self.taskDescription

    def getTaskDuration(self):
        return self.taskDuration

    def getTaskCompletionStatus(self):
        return self.isCompleted

    def getTaskCompletionTime(self):
        return self.completedAt

    def getTaskCreationTime(self):
        return self.createdAt

    def getTaskEstimatedDuration(self):
        return self.estimatedDuration

    def getTaskStartTime(self):
        return self.startedAt

    def getTaskIsDeleted(self):
        return getattr(self, 'isDeleted', False)

    def __eq__(self, other):
        if isinstance(other, TodoItem):
            return self.taskName == other.taskName
        if isinstance(other, str):
            return self.taskName == other
        return False

    def __hash__(self):
        return hash(self.taskName)