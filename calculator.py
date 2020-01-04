import re
print("This is my calculator")
print("Welcome")

run=True
previous=0

def my_calc():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter equation=")
    else:
        equation=input(str(previous))
    if equation=='quit':
        run=False
    else:
        equation=re.sub('A-Za-z/" "(),','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

while run:
    my_calc()


