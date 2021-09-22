class BeanFactory:
    def __init__(self, inital_beans=0):
        self.current_beans = inital_beans

    def cook_bean(self):
        self.current_beans += 1

    def eat_bean(self):
        self.current_beans -= 1

    def get_beans(self):
        return self.current_beans
