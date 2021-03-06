import os.path
import sys
import input
import tree
from asciitree import LeftAligned
# asciitree package Repository:     https://github.com/mbr/asciitree
# asciitree package documentation:  http://pythonhosted.org/asciitree/
from collections import OrderedDict as OD

# Check if input file exists
if not os.path.isfile('input.txt'):
    sys.exit("input.txt file does not exist.")
# Read tasks informations from input.txt using input module
try:
    tasks = input.file_to_tasks('input.txt')
except:
    sys.exit("Error happened in reading from input.txt")

# Get preq tree from tasks - using tree module
tree = tree.tree_from_tasks(tasks[:])

# Ordered Tasks
orderedTasks = []

# List of available tasks
availableTasks = [task for task in tasks if task[1] == "Start"]

# While all tasks are not scheduled
while len(orderedTasks) != len(tasks):
    # Sort available tasks based on their required time
    availableTasks.sort(key=lambda task: task[2])
    # Minimum time required task
    minTask = availableTasks[0]
    # Add the minimum required time task to the ordered task
    orderedTasks.append(minTask)
    # Remove the task from available tasks
    del availableTasks[0]
    # Add all task childs to available task
    for task in tree[minTask[0]]:
        task = [t for t in tasks if t[0] == task][0]
        availableTasks.append(task)

print("Order of tasks:")
for task in orderedTasks:
    print(str(task[0]))

totalCost = 0
spentTime = 0
for task in orderedTasks:
    spentTime += task[2]
    totalCost += spentTime * task[3]
print("Total cost = " + str(totalCost))

print("Prerequisite tree:")

displayTree = {}
dependantTasks = [task for task in tasks if task[1] == "Start"]

def recDraw(root):
    childsList = [task for task in tasks if task[1] == root[0]]
    childs = OD()
    for child in childsList:
        childs[child[0]] = recDraw(child[0])
    return childs

if len(dependantTasks) == 1:
    displayTree[dependantTasks[0]] = recDraw(dependantTasks[0])
else:
    od = OD()
    for task in dependantTasks:
        od[task[0]] = recDraw(task[0])
    displayTree = {'root': od}

tr = LeftAligned()
print tr(displayTree)

