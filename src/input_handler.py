from models import Mode


def create_mode() -> Mode:
    mode_name = input("Enter Mode name: ")
    mode = Mode(mode_name)
    return mode


def remove_mode(mode_list: list[Mode]) -> None:
    for i in range(len(mode_list)):
        print(f"{i}. {mode_list[i].mode_name}")
    mode_choice = input("remove mode: ")
    mode_list.remove(mode_list[int(mode_choice)])


def create_task() -> str:
    task = input("enter the task: ")
    return task


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

# Testing Program
# Computer_Mode = Mode("Computer Mode")
# Theory_Mode = Mode("Theory Mode")
# test_list = [Computer_Mode, Theory_Mode]
# temp = choose_mode(test_list)
# print(f"You have selected: {temp.mode_name}")
