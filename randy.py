import sys

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


for line in code.split('\n'):
    print(line + "\\n")
