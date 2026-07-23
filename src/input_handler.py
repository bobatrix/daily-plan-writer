from models import Mode, Subject


def create_mode() -> Mode:
    mode_name = input("Enter Mode name: ")
    mode = Mode(mode_name)
    return mode


def remove_mode(mode_list: list[Mode]) -> None:
    for i , mode in enumerate(mode_list):
        print(f"{i}. {mode.mode_name}")
    mode_choice = int(input("remove mode: "))
    mode_list.remove(mode_list[mode_choice])


def create_task(task_list: list[str]) -> list[str]:
    task_list.append(input("enter the task: "))
    return task_list


def create_subject() -> Subject:
    subject_name = input("enter the subject: ")
    subject = Subject(subject_name)
    return subject

def remove_subject(subject_list: list[Subject]) -> None:
    for i, subject in enumerate(subject_list):
        print(f"{i}. {subject.subject_name}")
    subject_choice = int(input("choose subject: "))
    subject_list.remove(subject_list[subject_choice])


def remove_task(task_list: list[str]) -> None:
    for i, task in enumerate(task_list):
        print(f"{i}. {task}")
    task_choice = int(input("remove task: "))
    task_list.remove(task_list[task_choice])


def choose_mode(mode_list: list[Mode]) -> Mode:
    while True:
        for i, mode in enumerate(mode_list):
            print(f"{i}. {mode.mode_name}")

        print(f"{len(mode_list)}. Create Mode \n{len(mode_list) + 1}. Delete Mode")

        mode_choice = int(input("choose mode: "))

        if mode_choice == len(mode_list):
            mode_list.append(create_mode())

        elif mode_choice == len(mode_list) + 1:
            remove_mode(mode_list)

        elif 0 <= mode_choice < len(mode_list):
            return mode_list[mode_choice]
        else:
            print("invalid choice")


def choose_subject(subject_list: list[Subject]) -> Subject:
    while True:
        for i, subject in enumerate(subject_list):
            print(f"{i}. {subject.subject_name}")

        print(f"{len(subject_list)}. Create Subject\n{len(subject_list) + 1}. Delete Subject")
        subject_choice = int(input("choose subject: "))
        if subject_choice == len(subject_list):
            subject_list.append(create_subject())
        elif subject_choice == len(subject_list) + 1:
            remove_subject(subject_list)

        elif 0 <= subject_choice < len(subject_list):
            return subject_list[subject_choice]

        else:
            print("invalid choice")




# Testing Program
# Computer_Mode = Mode("Computer Mode")
# Theory_Mode = Mode("Theory Mode")
# test_list = [Computer_Mode, Theory_Mode]
# temp = choose_mode(test_list)
# print(f"You have selected: {temp.mode_name}")
