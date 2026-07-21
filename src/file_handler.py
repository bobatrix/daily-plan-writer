from mdutils import MdUtils


def init_file(day_number: int) -> None:
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    file_name  = f"Day{day_number}Plan.md"
    day_name = day_list[(day_number - 3) % 7]
    title = f"{day_name} (Day {day_number})"

    mdFile = MdUtils(file_name=file_name, title=title)
    mdFile.new_line("---")

    mdFile.create_md_file()

init_file(3)
