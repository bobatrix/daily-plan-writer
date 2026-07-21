class Mode:
    def __init__(self, mode_name):
        self.mode_name = mode_name
        self.subject_list = []

    def add_subject(self, subject):
        self.subject_list.append(subject)
    def remove_subject(self, subject):
        self.subject_list.remove(subject)
    def get_subject_list(self):
        return self.subject_list


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.task_list = []

    def add_task(self, task: str):
        task = f"> * [ ] {task}"
        self.task_list.append(task)

    def get_task_list(self):
        return self.task_list
