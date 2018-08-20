import sys
import re
import random

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


def randomNameF():
    with open("data/femalenames.txt", 'r') as f:
        data = f.read().split("\n")
    return random.choice(data)

def randomNameM():
    with open("data/malenames.txt", 'r') as f:
        data = f.read().split("\n")
    return random.choice(data)

def randomName():
    with open("data/names.txt", 'r') as f:
        data = f.read().split("\n")
    return random.choice(data)

def randomAnimal():
    with open("data/animals.txt", 'r') as f:
        data = f.read().split("\n")
    return random.choice(data)

def randomCountry():
    with open("data/countries.txt", 'r') as f:
        data = f.read().split("\n")
    return random.choice(data)

def randomDigit():
    return str(random.randint(0, 9))

generators = {
    "animal": randomAnimal,
    "digit": randomDigit,
    "country": randomCountry,
    "femalename": randomNameF,
    "malename": randomNameM,
    "name": randomName
}


output = code

offset = 0
randomSomething = re.finditer(r"\$\w?\[[^\[\]]*\]", output)
for match in randomSomething:
    start = match.span()[0]+offset
    stop = match.span()[1]+offset
    command = output[start:stop].strip("$")
    caseMode = command[0].lower()
    generator = command[1:].strip('[]').lower()
    if caseMode == 'u':
        randomString = generators[generator]().upper()
    elif caseMode == 't':
        randomString = generators[generator]().title()
    elif caseMode == 'l':
        randomString = generators[generator]().lower()
    else:
        randomString = generators[generator]() #default
    output = output[0:start] + randomString + output[stop:]
    offset -= ((stop-start)-len(randomString))

offset = 0
makeChoice = re.finditer(r"\([^\(\)]*\)", output)
for match in makeChoice:
    start = match.span()[0]+offset
    stop = match.span()[1]+offset
    options = output[start:stop].strip("()").split("|")
    choiceString = random.choice(options)
    output = output[0:start] + choiceString + output[stop:]
    offset -= ((stop-start)-len(choiceString))

offset = 0
randomNumber = re.finditer(r"\{[^\{\}]*\}", output)
for match in randomNumber:
    start = match.span()[0]+offset
    stop = match.span()[1]+offset
    min, max = [int(n) for n in output[start:stop].strip("{}").split("/")]
    number = random.randint(min, max)
    output = output[0:start] + str(number) + output[stop:]
    offset -= ((stop-start)-len(str(number)))

sys.stdout.write(output)
