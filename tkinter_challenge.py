import tkinter as tk

expression = []


def buttonNum(number, equation):
    if expression[-1:] and expression[-1:][0].isnumeric():
        expression[-1:] = expression[-1:][0] + str(number)
    else:
        expression.append(str(number))
    print(expression)
    equation.set("".join(expression))


def buttonOp(operation, equation):
    if expression[-1:] and not expression[-1:][0].isnumeric():
        expression[-1:] = [str(operation)]
    else:
        expression.append(str(operation))
        equation.set("".join(expression))


def buttonEqual(equation):
    try:
        equation.set(str(eval(equation.get())))
    except:
        equation.set("It's an invalid expression")
        expression.clear()
        equation.set("Please enter an expression")


def buttonClear(equation):
    expression.clear()
    equation.set("Please enter an expression")


def buttonClearEntry(equation):
    del expression[-1:]
    equation.set("".join(expression))


def quit():
    calcWindow.destroy()


if __name__ == "__main__":
    calcWindow = tk.Tk()
    calcWindow.title("Calculator Xpro")
    calcWindow.geometry('450x275-8-200')
    calcWindow['padx'] = 8
    calcWindow.minsize(400, 250)
    calcWindow.maxsize(500, 325)
    calcWindow.configure(bg=input("Please enter a background color for the calculator: "))

    keysFgColor = input("Please enter a foreground color for the keys: ")

    equation = tk.StringVar()
    display = tk.Entry(calcWindow, textvariable=equation)
    display.place(height=100)
    display.grid(columnspan=4, ipadx=100, ipady=4)
    equation.set("Please enter an expression")

    quitButton = tk.Button(calcWindow, text='Quit', command=lambda: quit(), width=3, height=1)
    quitButton.grid(row=1, column=4)
    quitButton.configure(fg=keysFgColor)

    clearButton = tk.Button(calcWindow, text='C', command=lambda: buttonClear(equation), width=5, height=1)
    clearEntryButton = tk.Button(calcWindow, text='CE', command=lambda: buttonClearEntry(equation), width=5)
    leftBracketButton = tk.Button(calcWindow, text='(', command=lambda: buttonOp('(', equation), width=5, height=1)
    rightBracketButton = tk.Button(calcWindow, text=')', command=lambda: buttonOp(')', equation), width=5, height=1)

    clearButton.grid(row=1, column=0)
    clearButton.configure(fg=keysFgColor)
    clearEntryButton.grid(row=1, column=1)
    clearEntryButton.configure(fg=keysFgColor)
    leftBracketButton.grid(row=1, column=2)
    leftBracketButton.configure(fg=keysFgColor)
    rightBracketButton.grid(row=1, column=3)
    rightBracketButton.configure(fg=keysFgColor)

    sevenButton = tk.Button(calcWindow, text='7', command=lambda: buttonNum(7, equation), width=5, height=1)
    eightButton = tk.Button(calcWindow, text='8', command=lambda: buttonNum(8, equation), width=5, height=1)
    nineButton = tk.Button(calcWindow, text='9', command=lambda: buttonNum(9, equation), width=5, height=1)
    plusButton = tk.Button(calcWindow, text='+', command=lambda: buttonOp('+', equation), width=5, height=1)

    sevenButton.grid(row=2, column=0)
    sevenButton.configure(fg=keysFgColor)
    eightButton.grid(row=2, column=1)
    eightButton.configure(fg=keysFgColor)
    nineButton.grid(row=2, column=2)
    nineButton.configure(fg=keysFgColor)
    plusButton.grid(row=2, column=3)
    plusButton.configure(fg=keysFgColor)

    fourButton = tk.Button(calcWindow, text='4', command=lambda: buttonNum(4, equation), width=5, height=1)
    fiveButton = tk.Button(calcWindow, text='5', command=lambda: buttonNum(5, equation), width=5, height=1)
    sixButton = tk.Button(calcWindow, text='6', command=lambda: buttonNum(6, equation), width=5, height=1)
    minusButton = tk.Button(calcWindow, text='-', command=lambda: buttonOp('-', equation), width=5, height=1)

    fourButton.grid(row=3, column=0)
    fourButton.configure(fg=keysFgColor)
    fiveButton.grid(row=3, column=1)
    fiveButton.configure(fg=keysFgColor)
    sixButton.grid(row=3, column=2)
    sixButton.configure(fg=keysFgColor)
    minusButton.grid(row=3, column=3)
    minusButton.configure(fg=keysFgColor)

    oneButton = tk.Button(calcWindow, text='1', command=lambda: buttonNum(1, equation), width=5, height=1)
    twoButton = tk.Button(calcWindow, text='2', command=lambda: buttonNum(2, equation), width=5, height=1)
    threeButton = tk.Button(calcWindow, text='3', command=lambda: buttonNum(3, equation), width=5, height=1)
    multiplyButton = tk.Button(calcWindow, text='x', command=lambda: buttonOp('*', equation), width=5, height=1)

    oneButton.grid(row=4, column=0)
    oneButton.configure(fg=keysFgColor)
    twoButton.grid(row=4, column=1)
    twoButton.configure(fg=keysFgColor)
    threeButton.grid(row=4, column=2)
    threeButton.configure(fg=keysFgColor)
    multiplyButton.grid(row=4, column=3)
    multiplyButton.configure(fg=keysFgColor)

    zeroButton = tk.Button(calcWindow, text='0', command=lambda: buttonNum(0, equation), width=5, height=1)
    decimalButton = tk.Button(calcWindow, text='.', command=lambda: buttonNum('.', equation), width=5, height=1)
    equalButton = tk.Button(calcWindow, text='=', command=lambda: buttonEqual(equation), width=5, height=1)
    divideButton = tk.Button(calcWindow, text='/', command=lambda: buttonOp('/', equation), width=5, height=1)

    zeroButton.grid(row=5, column=0)
    zeroButton.configure(fg=keysFgColor)
    decimalButton.grid(row=5, column=1)
    decimalButton.configure(fg=keysFgColor)
    equalButton.grid(row=5, column=2)
    equalButton.configure(fg=keysFgColor)
    divideButton.grid(row=5, column=3)
    divideButton.configure(fg=keysFgColor)

    calcWindow.mainloop()


