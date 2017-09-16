class Subject:
    def __init__(self, name, *args_list):
        self.name = name
        self.rating = list(args_list)
    def countAverageRating (self):
        sum = 0
        for x in range(len(self.rating)):
            sum = sum + self.rating[x]
        return sum/len(self.rating)