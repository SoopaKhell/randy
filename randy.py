import sys
import re
import random

print(sys.argv)

modes = []

code = None

if len(sys.argv) > 1:
    if sys.argv[1] == "-e":
        if len(sys.argv) == 3:
            print("Output for \"" + sys.argv[2] + "\":")
            code = sys.argv[2]
        elif len(sys.argv) > 3:
            print("Error: Too many arguments for option '" + sys.argv[1] + "'. Remember to use quotes!")
        else:
            print("Error: Option '" + sys.argv[1] + "' was given but no further arguments were found. Put the code after '-e'.")
    else: #no other args (default action)
        if sys.argv[1].endswith(".ry"):
            try:
                with open(sys.argv[1], 'r') as c:
                    print("Output for \"" + sys.argv[1] + "\":")
                    code = c.read()
            except:
                print("Error: File not found.")
        else:
            print("Error: Invalid filetype! Must be a .ry file.")


#print(code.split("\n"))

parsedLines = []

for line in code.split('\n'):
    randomNumber = re.search(r"\{\d+-\d+\}", line)
    if randomNumber:
        start, stop = randomNumber.span()
        min, max = [int(n) for n in line[start:stop].strip("{}").split("-")]
        number = random.randint(min ,max)
        parsedLine = line[0:start] + str(number) + line[stop:]
        parsedLines.append(parsedLine)
    else:
        parsedLines.append(line)


output = '\n'.join(parsedLines)
print(output)
