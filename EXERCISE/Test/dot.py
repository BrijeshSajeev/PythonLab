# import tkinter as tk


# def draw_dot():
#     diameter = 50  # Diameter of the dot
#     x = 50  # x-coordinate of the dot's center
#     y = 50  # y-coordinate of the dot's center
#     canvas.create_oval(x, y, x + diameter, y + diameter, fill="red")


# root = tk.Tk()
# root.title("Red Dot Example")

# canvas = tk.Canvas(root, width=200, height=200)
# canvas.pack()

# button = tk.Button(root, text="Draw Dot", command=draw_dot)
# button.pack()

# root.mainloop()


import turtle

t = turtle.Turtle()


t.dot(20, "blue")


t.hideturtle()
turtle.done()
