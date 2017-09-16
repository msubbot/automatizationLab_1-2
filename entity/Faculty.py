class Faculty:
    def __init__(self, name, *args_list):
        self.name = name
        self.groups = list(args_list)