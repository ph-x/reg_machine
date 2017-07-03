import parsing
import sys
max = 0
commands = []
file = open(sys.argv[1], 'r')
for line in file:
    cmd = parsing.command(line)
    commands.append(cmd)
    for arg in cmd.args[1:]:
        if arg > max:
            max = arg
tape = [0 for i in range(max)]
for i in range(2, len(sys.argv)):
    tape[i-1] = int(sys.argv[i])
k = 0
count = 0
MAXCOUNT = 100000000
inf = sys.maxsize
while k < len(commands):
    count = count + 1
    if count >= MAXCOUNT:
        tape[0] = inf
        break
    command = commands[k]
    if command.cmd == 'z':
        tape[command.args[1]] = 0
    elif command.cmd == 'j':
        if tape[command.args[1]] == tape[command.args[2]]:
            k = command.args[3]
            continue
    elif command.cmd == 's':
        tape[command.args[1]] = tape[command.args[1]] + 1
    k = k + 1

print(tape[0])
