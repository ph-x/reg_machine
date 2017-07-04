def parse(command):
    args = command.split(' ')
    cmd = args[0]
    if cmd != '#':
        init = 1
    else:
        return cmd, args
    for i in range(init, len(args)):
        args[i] = int(args[i])
    return cmd, args
class command:
    def __init__(self, content):
        self.content = content
        self.cmd, self.args = parse(content)
    def display(self):
        print(self.content)
    def max_reg(self):
        if self.cmd == 's' or self.cmd == 'z':
            return self.args[1]
        elif self.cmd == 'j' or self.cmd == 'asn':
            return max(self.args[1], self.args[2])
        elif self.cmd == '#':
            return 0
        else:
            return max(self.args[1:])
