# import modules
# from tkinter import Tk, Frame, Canvas, CENTER, Button, NW, Label, SOLID
from tkinter import colorchooser, filedialog
# OptionMenu, messagebox
from tkinter import DOTBOX, StringVar
# simpledialog

import os
import pickle

prev_Point = [0, 0]
current_Point = [0, 0]
penColor = "black"
pencilWidth = 1
shapeList = ["Line", "Square", "Round", "Arrow", "Diamond"]
shapeFill = "black"
canvas_data = []


class Draw:
    def __init__(self, canvas):

        self.canvas = canvas
        self.shapeSelect = StringVar()
        self.shapeSelect.set("Line")
        self.selected_pen_type = "pen"
        self.colour_choice = StringVar()

        self.canvas.grid(row=1, column=4, rowspan=15, columnspan=15)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

    def pencil_width_i(self):
        global pencilWidth
        if pencilWidth != 10:
            pencilWidth += 1

        else:
            pencilWidth = pencilWidth

    # Decrease pencilWidth Size By 1
    def pencil_width_d(self):
        global pencilWidth
        if pencilWidth != 1:
            pencilWidth -= 1

        else:
            pencilWidth = pencilWidth

    def pencil_width_df(self):
        global pencilWidth
        self.shapeSelect.set("Line")
        pencilWidth = 1

    # Pencil
    def pencil(self):
        global penColor

        penColor = "black"
        self.canvas["cursor"] = "pencil"

    # Eraser
    def eraser(self):
        self.shapeSelect.set("Eraser")
        selected_pen_type = "Eraser"
        self.canvas.bind("<Button-1>", self.paint)

    # Pencil Choose Color
    def colorChoice(self):
        global penColor

        color = colorchooser.askcolor(title="Select a Color")
        self.canvas["cursor"] = "pencil"

        if color[1]:
            penColor = color[1]

        else:
            pass

    # Shape Color Chooser
    def shapeColorChoice(self):
        global shapeFill

        color = colorchooser.askcolor(title="Select a Color")
        self.canvas["cursor"] = "pencil"

        if color[1]:
            shapeFill = color[1]

        else:
            shapeFill = "black"

    # Paint Function
    def paint(self, event):
        global prev_Point
        global current_Point
        global pencilWidth
        x = event.x
        y = event.y
        shape = self.shapeSelect.get()
        current_Point = [x + pencilWidth, y + pencilWidth]

        if shape == "Line":
            if prev_Point != [0, 0]:
                self.canvas["cursor"] = "pencil"
                if self.selected_pen_type == "pen":
                    self.canvas.create_line(prev_Point[0], prev_Point[1], x, y, fill=penColor,
                                            width=pencilWidth, smooth=True)
        elif shape == "Square":
            if prev_Point != [0, 0]:
                self.canvas["cursor"] = "draped_box"
                if self.selected_pen_type == "pen":
                    self.canvas.create_rectangle(prev_Point[0], prev_Point[1], current_Point[0], current_Point[1],
                                                 fill=shapeFill,
                                                 outline=penColor)
        elif shape == "Arrow":
            self.canvas["cursor"] = "ll_angle"
            if prev_Point != [0, 0]:
                if self.selected_pen_type == "pen":
                    self.canvas.create_polygon(prev_Point[0], prev_Point[1], prev_Point[0], current_Point[1], x,
                                               current_Point[1], fill=shapeFill,
                                               outline=penColor)
        elif shape == "Round":
            self.canvas["cursor"] = "circle"
            if prev_Point != [0, 0]:
                if self.selected_pen_type == "pen":
                    self.canvas.create_oval(prev_Point[0], prev_Point[1], current_Point[0], current_Point[1],
                                            fill=shapeFill,
                                            outline=penColor)

        elif shape == "Diamond":
            self.canvas["cursor"] = "diamond_cross"
            if prev_Point != [0, 0]:
                if self.selected_pen_type == "pen":
                    self.canvas.create_polygon(x - pencilWidth, y, x, y - pencilWidth, x + pencilWidth, y, x,
                                               y + pencilWidth, fill=shapeFill, outline=penColor)


        elif shape == "Eraser":
            pencilWidth = 10
            if prev_Point != [0, 0]:
                self.canvas["cursor"] = DOTBOX
                self.canvas.create_rectangle(prev_Point[0], prev_Point[1], x, y, fill="white",
                                             outline="white")

        prev_Point = [x - pencilWidth, y - pencilWidth]
        if event.type == "5":
            prev_Point = [0, 0]

    # Close App
    def newApp(self):
        os.startfile("draw.py")

    # Clear Screen
    def clearScreen(self):
        self.canvas.delete("all")

    # Save Images
    def saveImg(self):
        global canvas_data

        for obj in self.canvas.find_all():
            obj_type = self.canvas.type(obj)
            color = self.canvas.itemcget(obj, "fill")
            coords = self.canvas.coords(obj)
            canvas_data.append({"type": obj_type, "color": color, "coords": coords})

        # Saving the canvas data to ects files
        file_path = filedialog.asksaveasfilename(
            defaultextension=".ects",
            filetypes=[
                ("ECTS files", "*.ects"),
                ("PNG files", "*.png"),
                ("JPG files", "*.jpg"),
            ],
        )
        if file_path:
            with open(file_path, "wb") as file:
                pickle.dump(canvas_data, file)

            # print("Your file {} has been saved".format(file))

    # Opening already or earlier made ects files
    def openImg(self):
        global canvas_data
        file_path = filedialog.askopenfilename(
            defaultextension=".ects",
            filetypes=[
                ("ECTS files", "*.ects"),
                ("PNG files", "*.png"),
                ("JPG files", "*.jpg"),
            ],
        )
        if file_path:
            with open(file_path, "rb") as file:
                canvas_data = pickle.load(file)

        # redrawing
        self.canvas.delete("all")
        # Draw objects from canvas_data
        for obj in canvas_data:
            color = obj["color"]
            coords = obj["coords"]
            self.canvas.create_polygon(coords, fill=color, outline=color, width=pencilWidth)

# class Popup(Draw):
#     def __init__(self, cvas):
#         super().__init__(cvas)
#         self.cvas = cvas
#         self.popup_menu = Menu(self.cvas)
#
#         self.popup_menu.add_command(label="save", command=self.saveImg)
#         self.popup_menu.add_command(label="Copy", command=self.edit_copy)
#         self.popup_menu.add_command(label="Cut", command=self.edit_cut)
#         self.popup_menu.add_command(label="Paste", command=self.edit_paste)
#         self.popup_menu.add_command(label="Find", command=self.edit_find)
#         self.popup_menu.add_separator()
#     #    self.popup_menu.add_command(label="Help", command=self.help_open_help)
#         self.window.bind("<Button-3>", self.popup_menu_event)
#
#     def popup_menu_event(self, event):
#         # find the x and y positions where the user clicked the right mouse button
#         x_position_of_click = event.x_root
#         y_position_of_click = event.y_root
#         # post/place the pop menu where the user clicked.
#         self.popup_menu.post(x_position_of_click, y_position_of_click)
#
#     def edit_cut(event):
#         pass
#
#     def edit_cut(event):
#         pass
#
#     def edit_copy(event):
#         pass
#
#     def edit_paste(event):
#         pass
#
#     def edit_find(event):
#         pass
