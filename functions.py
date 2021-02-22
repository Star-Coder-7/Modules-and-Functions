def python_food():
    width = 100
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (100 - len(text)) // 2
    return " " * left_margin + text


# with open("centered", mode='w') as centeredFile:
# Calling the function
# s1 = centre_text("Spam and eggs")
# print(s1)
# s2 = centre_text("Python is powerful")
# print(s2)
# s3 = centre_text(13)
# print(s3)
# s4 = centre_text("Python likes spam and eggs")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
# print(s5)

with open("menu", 'w+') as menu:
    s1 = centre_text("Spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("Python is powerful")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("Python likes spam and eggs"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
    print(s5, file=menu)

