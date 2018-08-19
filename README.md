# Randy
A scripting language used to generate random outputs.
This is an early stage of Randy and there are few features.

# Usage
Randy scripts are always .ry files. To execute it, run:
```
python randy.py {filename.ry}
```
(<a href="https://www.python.org/downloads/">Python 3</a> must be used)


# Basic Syntax
Randy has a simple method to generate random numbers. Curly brackets surround two numbers separated by a forward-slash.
```
I have {2/3} children.
```

The range is inclusive, so this could output either:
`I have 2 children`
or
`I have 3 children`

To have Randy choose one of multiple things, use parenthesis and separate the choices with "|".
```
I like (apples|oranges|ninjas).
```

Possible outputs include:
```
I like apples.
I like oranges.
I like ninjas.```
