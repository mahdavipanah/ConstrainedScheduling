from os import linesep
import re

def file_to_tasks(filename):
    # List of tasks
    tasks = []

    with open(filename) as input_file:
        # Regex pattern for excluding white spaces
        pattern = re.compile(r'\s+')
        # For every line in input file
        for line in input_file:
            # If line is empty
            if re.sub(pattern, '', line) == '':
                # Stop reading from input file
                break
            else:
                tasks.append(line.rstrip(linesep).split(' '))

        for task in tasks:
            task[2] = int(task[2])
            task[3] = int(task[3])

        return tasks