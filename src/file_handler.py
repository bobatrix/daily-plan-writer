from mdutils import MdUtils


def init_file(day_number: int) -> MdUtils:
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    file_name = f"Day{day_number}Plan.md"
    day_name = day_list[(day_number - 3) % 7]
    title = f"{day_name} (Day {day_number})"

    mdFile = MdUtils(file_name=file_name, title=title)
    mdFile.new_line("---\n\n")
    return mdFile

def file_writer(mdFile: MdUtils, content: str) -> MdUtils:
    mdFile.write(content)
    return mdFile



# file = init_file(3)
# file.write("> ### Python\n>\n> * [ ] Continue with something")
# file.create_md_file()
