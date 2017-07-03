def parse(command):
    args = command.split(' ')
    cmd = args[0]
    rargs = [-1, -1, -1, -1]
    rargs[1] = int(args[1])
    rargs[2] = -1
    rargs[3] = -1
    if len(args) > 2:
        rargs[2] = int(args[2])
    if len(args) > 3:
        rargs[3] = int(args[3])
    return cmd, rargs[1], rargs[2], rargs[3]
class command:
    def __init__(self, content):
        self.content = content
        self.args = [-1, -1, -1, -1]
        self.cmd, self.args[1], self.args[2], self.args[3] = parse(content)
        self.args[0] = self.cmd
    def display(self):
        print(self.content)
