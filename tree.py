# Add a task to tree and invoke yourself for every child of it
def addTaskPreq(taskName, tasks, tree):
    # Remove the task from tasks
    tasks = [task for task in tasks if task[0] != taskName]
    # Find all tasks with preq = taskName
    preqs = [task[0] for task in tasks if task[1] == taskName]
    # Add taskName to tree
    tree[taskName] = preqs
    for task in preqs:
        addTaskPreq(task[0], tasks, tree)

# Creates a tree from tasks
def tree_from_tasks(tasks):
    # Tree created from tasks
    tree = {}
    # Get tasks that have no prerequisites
    startTasksNames = [task[0] for task in tasks if task[1] == "Start"]
    # Add all start tasks to tree
    for taskName in startTasksNames:
        addTaskPreq(taskName, tasks, tree)
    return tree