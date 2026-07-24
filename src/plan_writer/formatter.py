from models import *


def mode_to_text(mode: Mode) -> str:
    output = ""
    output += "## " + mode.mode_name
    output += "\n"
    if mode.get_subject_list():
        for subject in mode.get_subject_list():
            if subject.get_task_list():
                output += "> ### " + subject.subject_name + "\n>\n"
                for task in subject.get_task_list():
                    output += "> * [ ] " + task + "\n"
                output += "\n"
        output += "---\n"
    else:
        raise "No subject list"
    return output

# # Test program IGNORE
# test_task_list = ["create test_task_list", "add test_task_list to subject", "add subject to mode"]
#
# test_subject1 = Subject(subject_name="Test1")
# test_subject1.add_task(test_task_list[0])
# test_subject1.add_task(test_task_list[1])
# test_subject1.add_task(test_task_list[2])
#
# test_subject2 = Subject(subject_name="Test2")
# test_subject2.add_task(test_task_list[0])
# test_subject2.add_task(test_task_list[1])
# test_subject2.add_task(test_task_list[2])
#
# test_subject3 = Subject(subject_name="Test3")
#
# test_mode = Mode(mode_name="Test")
# test_mode.add_subject(test_subject1)
# test_mode.add_subject(test_subject2)
# test_mode.add_subject(test_subject3)
#
# print(mode_to_text(test_mode))
