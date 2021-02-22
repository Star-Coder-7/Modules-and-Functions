import tkinter as tk


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, width=2,
                     outline=color)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    xOrigin = page.winfo_width() / 2
    yOrigin = page.winfo_height() / 2
    page.configure(scrollregion=(-xOrigin, -yOrigin, xOrigin, yOrigin))
    page.create_line(-xOrigin, 0, xOrigin, 0, fill='black')
    page.create_line(0, yOrigin, 0, -yOrigin, fill='black')
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')


mainWindow = tk.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

canvas = tk.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, 'green')
circle(canvas, 100, 100, -100, 'blue')
circle(canvas, 100, -100, 100, 'purple')
circle(canvas, 100, -100, -100, 'yellow')
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()












