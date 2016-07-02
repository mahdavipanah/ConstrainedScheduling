import os.path
import sys
import input

# Check if input file exists
if not os.path.isfile('input.txt'):
    sys.exit("input.txt file does not exist.")
# Read tasks informations from input.txt using input module
try:
    tasks = input.file_to_tasks('input.txt')
except:
    sys.exit("Error happened in reading from input.txt")