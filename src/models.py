class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.task_list = []

    def add_task(self, task: str) -> None:
        self.task_list.append(task)

    def get_task_list(self) -> list[str]:
        return self.task_list


class Mode:
    def __init__(self, mode_name):
        self.mode_name = mode_name
        self.subject_list = []

    def add_subject(self, subject: Subject) -> None:
        self.subject_list.append(subject)

    def remove_subject(self, subject: Subject) -> None:
        self.subject_list.remove(subject)

    def get_subject_list(self) -> list[Subject]:
        return self.subject_list
