# 1. Define a class named Task.
#
# __init__(self, title: str) -> None:
#   Store title as an instance attribute.
#   Set an instance attribute completed to False.
#
# complete(self) -> None:
#   Set this task's completed attribute to True.
#
# describe(self) -> str:
#   Return a string like:
#   "Learn Python | completed: False"
class Task:
    def __init__(self, title: str) -> None:
        self.title = title
        self.completed = False

    def complete(self) -> None:
        self.completed = True

    def describe(self) -> str: 
        return f"{self.title} | completed: {self.completed}"
    
# 2. Create two separate Task objects:
# task1: title "Learn Python"
# task2: title "Build API"
task1 = Task("Learn Python")
task2 = Task("Build API")

# 3. Call complete() on task1 only.
task1.complete()

# 4. Print both tasks' describe() results.
print(task1.describe())
print(task2.describe())

# 5. Should completing task1 also complete task2? Explain why.
# Answer: No task1 complete shouldn't complete task2 because each object have there own memory and class here work just as template


# Define PriorityTask, inheriting from Task.
#
# __init__(self, title: str, priority: int) -> None:
#   Use super().__init__(title) to initialise inherited attributes.
#   Store priority on this instance.
#
# Override describe(self) -> str:
#   Include title, completed and priority in the returned string.
class PriorityTask(Task): 
    def __init__(self, title: str, priority: int) -> None:
        super().__init__(title)
        self.priority = priority

    def describe(self) -> str:
        return f"{self.title}, Completed: {self.completed}, priority: {self.priority}"
    
# Create a PriorityTask with title "Build API" and priority 1.
# Call its inherited complete() method.
# Print its describe() result.
priority1 = PriorityTask("Build API", 1)
priority1.complete()
priorityRes = priority1.describe()
print(priorityRes)

# Does PriorityTask need its own complete() method to use it?
# Explain: No, It inherit the parent methods and properties and can use it no need to repeat it again.