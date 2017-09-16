class Student:
    def __init__(self, name, subname, *args_list):
        self.name = name
        self.subname = subname
        self.subjects = list(args_list)