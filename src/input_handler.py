def get_task():
    task = input("enter the task: ")
    return task

def choose_mode(mode_list):
    for i in range(len(mode_list)):
        print(str(i + 1) + " : " + mode_list[i])

def choose_subject(subject_list):
    for i in range(len(subject_list)):
        print(str(i + 1) + " : " + subject_list[i])

