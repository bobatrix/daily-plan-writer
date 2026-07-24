
from input_handler import *
from file_handler import *


mode_list = []

# day_number = int(input("Enter the day number: "))
# init_file(day_number)

ready_to_format = False

while not ready_to_format:

    mode = choose_mode(mode_list)

    subject = choose_subject(mode.get_subject_list())

    show_tasks(subject.get_task_list())

    if input("Are you ready to continue? (y/n): ").lower() == "y":
        ready_to_format = True


