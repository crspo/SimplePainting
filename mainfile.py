from tkinter import *
from tkinter import (Tk, Frame, Canvas, CENTER )
# , Button, NW, Label, SOLID
# from tkinter import colorchooser, filedialog, OptionMenu, messagebox
# from tkinter import DOTBOX, StringVar, simpledialog
from popup import Popup as p
from draw import Draw as d
#from draw import Popup as p

shapeList = ["None", "Square", "Round", "Arrow", "Diamond"]

class MainCanvas:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        #self.holder = holder
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.Popup = p(canvas)
        self.banner()

    def banner(self):
        file_menu = Menu(self.menu_bar)
        color_menu = Menu(self.menu_bar)
        tool_menu = Menu(self.menu_bar)
        view_menu = Menu(self.menu_bar)
        help_menu = Menu(self.menu_bar)
        save_submenu = Menu(file_menu)
        pencil_menu = Menu(tool_menu)
        shape_menu = Menu(self.menu_bar)
        self.paint = d(canvas)

        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.paint.openImg)
        file_menu.add_cascade(label="Save", menu=save_submenu)
        save_submenu.add_command(label="Save Image", command=self.paint.saveImg)
        #save_submenu.add_command(label="Save as...", command=self.paint.saveImg)
        file_menu.add_command(label="New", command=self.paint.newApp)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)

        self.menu_bar.add_cascade(label="Select Colors", menu=color_menu)
        color_menu.add_command(label="Shape Outline", command=self.paint.colorChoice)
        color_menu.add_command(label="Sape Fill", command=self.paint.shapeColorChoice)

        self.menu_bar.add_cascade(label="Tools", menu=tool_menu)
        tool_menu.add_cascade(label="Pencil", menu=pencil_menu)
        pencil_menu.add_command(label="Increase Pencil Size", command=self.paint.pencil_width_i)
        pencil_menu.add_command(label="Decrease Pencil Size", command=self.paint.pencil_width_d)
        pencil_menu.add_command(label="Default", command=self.paint.pencil_width_df)
        tool_menu.add_command(label="Eraser", command=self.paint.eraser)

        tool_menu.add_command(label="Clear", command=self.paint.clearScreen)
        tool_menu.add_separator()
        tool_menu.add_command(label="Find", command=self.find)

        self.menu_bar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Zoom in", command=self.view_zoom_in)
        view_menu.add_command(label="Zoom out", command=self.view_zoom_out)
        view_menu.add_separator()
        view_menu.add_command(label="View options", command=self.view_options)
        view_menu.add_separator()
        view_menu.add_command(label="Recent changes", command=self.view_recent_changes)

        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Getting started", command=self.help_getting_started)
        help_menu.add_command(label="Tip of the day", command=self.help_tip_of_day)
        help_menu.add_command(label="Open help", command=self.help_open_help)
        help_menu.add_command(label="Submit bug report", command=self.help_submit_bug_report)

        self.menu_bar.add_cascade(label="Shapes", menu=shape_menu)
        shape_menu.add_radiobutton(label='Line', variable=self.paint.shapeSelect, value='Line')
        shape_menu.add_radiobutton(label='Square', variable=self.paint.shapeSelect, value='Square')
        shape_menu.add_radiobutton(label='Round', variable=self.paint.shapeSelect, value='Round')
        shape_menu.add_radiobutton(label='Arrow', variable=self.paint.shapeSelect, value='Arrow')
        shape_menu.add_radiobutton(label='Diamond', variable=self.paint.shapeSelect, value='Diamond')

    # def FrameWidth(self, event):
    #     if event.width > self.mailbox_frame.winfo_width():
    #         self.canvas.itemconfig(self.canvas_frame, width=event.width - 4)
    #     if event.height > self.mailbox_frame.winfo_height():
    #         self.canvas.itemconfig(self.canvas_frame, height=event.height - 4)

    def find(event):
        pass

    def view_zoom_in(event):
        pass
    def view_zoom_out(event):
        pass
    def view_options(event):
        pass
    def view_recent_changes(event):
        pass

    def help_getting_started(event):
        pass
    def help_tip_of_day(event):
        pass
    def help_open_help(event):
        pass
    def help_submit_bug_report(event):
        pass


if __name__ == '__main__':
    window = Tk()
    window.title("Menu_Bar")
    window.geometry("1100x650")

    # Main Frame
    frame = Frame(window, height=500, width=1100)
    frame.grid(row=1, column=0)
    #frame.pack()
    # Making a Canvas
    canvas = Canvas(frame, height=450, width=1000, bg="white")
    canvas.grid(row=0, column=0)
    canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas.config(cursor="pencil")
    canvas.pack()

    MainCanvas(window, canvas)
    window.mainloop()


