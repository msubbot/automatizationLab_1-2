
class University:
    def __init__(self, name, *args_list):
        self.name = name
        self.faculties = list(args_list)