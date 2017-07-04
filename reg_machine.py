import parsing
import sys
register_machines = {}
number_of_spaces = 0
def display(msg):
    for i in range(number_of_spaces):
        print('    ', end='')
    print(msg)
class SIZE_LIMITS:
    MAX_REG_ALLOWED = 100
    MAX_RUN_TIME_ALLOWED = 100000000
class rm(SIZE_LIMITS):
    def __init__(self, file_name):
        self.file_name = file_name
        self.max_reg = 0
        self.commands = []
        register_machines[file_name] = self
        file = open(self.file_name, 'r')
        for line in file:
            cmd = parsing.command(line)
            if cmd.cmd == '#':
                new_rm = rm(cmd.args[1])
                continue
            self.commands.append(cmd)
            if cmd.max_reg() > self.max_reg:
                self.max_reg = cmd.max_reg()
        if self.max_reg > self.MAX_REG_ALLOWED:
            print('number of register used (' + self.max_reg +') is over the limit (' + self.MAX_REG_ALLOWED + ')')
            exit(0)
    def run(self, inputs):
        if self.max_reg < len(inputs):
            self.max_reg = len(inputs)
        self.tape = [0 for i in range(self.max_reg + 1)]
        for i in range(len(inputs)):
            self.tape[i+1] = int(inputs[i])
        display(self.file_name + ' begin')
        self.count = 0
        self.cmd_index = 0
        while self.cmd_index < len(self.commands):
            display(self.tape)
            self.count = self.count + 1
            if self.count >= self.MAX_RUN_TIME_ALLOWED:
                self.tape[0] = float('Inf')
                break
            current_command = self.commands[self.cmd_index]
            if current_command.cmd == 'z':
                self.tape[current_command.args[1]] = 0
            elif current_command.cmd == 'j':
                if self.tape[current_command.args[1]] == self.tape[current_command.args[2]]:
                    self.cmd_index = current_command.args[3]
                    continue
            elif current_command.cmd == 's':
                self.tape[current_command.args[1]] = self.tape[current_command.args[1]] + 1
            elif current_command.cmd == 'asn':
                self.tape[current_command.args[1]] = self.tape[current_command.args[2]]
            elif current_command.cmd in register_machines:
                args = []
                for arg in current_command.args[2:]:
                    args.append(self.tape[arg])
                global number_of_spaces
                number_of_spaces = number_of_spaces + 1
                self.tape[current_command.args[1]] = register_machines[current_command.cmd].run(args)
                number_of_spaces = number_of_spaces - 1
            else:
                print('unrecognized command: ' + current_command.cmd)
                exit(0)
            self.cmd_index = self.cmd_index + 1
        display(self.tape)
        display(self.file_name + ' end')
        return self.tape[0]

main = rm(sys.argv[1])
result = main.run(sys.argv[2:])
print(result)
exit(0)
