class Todo:
    def __init__(self, have_to_do):
        self.task = have_to_do
        self.complete = False

    def finish(self):
        self.complete = True


x = input("in")
a = Todo(x)

print(a.complete)
print(a.task)
