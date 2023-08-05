# heStudio Framework

# show框架

def show(message: str = "", title: str = ""):
    import heframework.src.show
    heframework.src.show.show(message, title).show()

# list_command框架


def list_command(mode:str="list",json_file: str = "", info: str = "",name: list = [], command: list = []):
    import heframework.src.list_json
    import heframework.src.list_list
    if mode == "list":
        heframework.src.list_list.list(name, command, info).list()
    elif mode == "json":
        heframework.src.list_json.list(json_file, info).list()
