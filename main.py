from datetime import datetime

class TodoItem:
    # Task Name
    taskName = ""
    # Task Description
    taskDescription = ""
    # Task Category
    taskCategory = ""
    # Task Priority
    taskPriority = 0
    # Task Difficulty
    taskDifficulty = 0
    # Task Duration
    taskDuration = 0
    # Task Completion Status
    isCompleted = False
    # Task Completion Time
    completedAt = None
    # Task Creation Time
    createdAt = None
    # Task Estimated Duration
    estimatedDuration = 0
    # Task Start Time
    startedAt = None
    
    # Constructor
    def __init__(self, taskName, isCompleted=False, taskPriority=0, taskDifficulty=0, taskDuration=0, taskCategory="", taskDescription="", estimatedDuration=0):
        self.taskName = taskName
        self.isCompleted = isCompleted
        self.createdAt = datetime.now()
        self.completedAt = None
        self.startedAt = None
        self.estimatedDuration = estimatedDuration
        self.taskDuration = taskDuration
        self.taskPriority = taskPriority
        self.taskDifficulty = taskDifficulty
        self.taskCategory = taskCategory
        self.taskDescription = taskDescription

    def __str__(self):
        return f"Task Name: {self.taskName}\nTask Priority: {self.taskPriority}\nTask Difficulty: {self.taskDifficulty}\nTask Category: {self.taskCategory}\nTask Description: {self.taskDescription}\nTask Duration: {self.taskDuration}\nTask Completion Status: {self.isCompleted}\nTask Completion Time: {self.completedAt}\nTask Creation Time: {self.createdAt}\nTask Estimated Duration: {self.estimatedDuration}\nTask Start Time: {self.startedAt}"

# Main Function
def main():
    todo_list = []
    print("Hello World")
    while True:
        user_input = input("Enter a task (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        todo_list.append(TodoItem(user_input, False, 0, 0, 0, "", "", 0))
        print(todo_list[-1])

# Entry Point
if __name__ == "__main__":
    main()