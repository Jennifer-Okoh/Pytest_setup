
class Reminder:
    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        return f"{self.task}, {self.name}!"
    
# Look here! We want to fail if there is no reminder yet.
    # def remind(self):
    #     if self.task is None:
    #         raise Exception("No reminder set!")
    #     return f"{self.task}, {self.name}!"
    

    