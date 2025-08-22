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
    
    # Pure setters (no I/O) used by CLI layer
    def set_name(self, name: str):
        self.taskName = name

    def set_priority(self, priority: int):
        self.taskPriority = priority

    def set_difficulty(self, difficulty: int):
        self.taskDifficulty = difficulty

    def set_duration(self, duration: int):
        self.taskDuration = duration

    def set_category(self, category: str):
        self.taskCategory = category

    def set_description(self, description: str):
        self.taskDescription = description

    def set_estimated_duration(self, estimated: int):
        self.estimatedDuration = estimated

    def completeTask(self):
        self.isCompleted = True
        self.completedAt = datetime.now()
    
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