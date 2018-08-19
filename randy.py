import sys
import re
import random

#print(sys.argv)

modes = []

code = None

if len(sys.argv) > 1:
    if sys.argv[1] == "-e":
        if len(sys.argv) == 3:
            code = sys.argv[2]
        elif len(sys.argv) > 3:
            print("Error: Too many arguments for option '" + sys.argv[1] + "'. Remember to use quotes!")
        else:
            print("Error: Option '" + sys.argv[1] + "' was given but no further arguments were found. Put the code after '-e'.")
    else: #no other args (default action)
        if sys.argv[1].endswith(".ry"):
            try:
                with open(sys.argv[1], 'r') as c:
                    code = c.read()
            except:
                print("Error: File not found.")
        else:
            print("Error: Invalid filetype! Must be a .ry file.")


#print(code.split("\n"))

parsedLines = []

for line in code.split('\n'):
    offset = 0
    randomNumber = re.finditer(r"\{[^\{\}]*\}", line)
    for match in randomNumber:
        start = match.span()[0]+offset
        stop = match.span()[1]+offset
        min, max = [int(n) for n in line[start:stop].strip("{}").split("/")]
        number = random.randint(min, max)
        line = line[0:start] + str(number) + line[stop:]
        offset -= ((stop-start)-len(str(number)))

    offset = 0
    makeChoice = re.finditer(r"\([^\(\)]*\)", line)
    for match in makeChoice:
        start = match.span()[0]+offset
        stop = match.span()[1]+offset
        options = line[start:stop].strip("()").split("|")
        choiceString = random.choice(options)
        line = line[0:start] + choiceString + line[stop:]
        offset -= ((stop-start)-len(choiceString))
    parsedLines.append(line)


output = '\n'.join(parsedLines)
print(output)
