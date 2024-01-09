from tkinter import *
#from draw import Draw as d

class Popup():
    def __init__(self, parent):
        self.window = parent
        self.popup_menu = Menu(self.window)

        #self.popup_menu.add_command(label="save", command=self.d.saveImg)
        self.popup_menu.add_command(label="Copy", command=self.edit_copy)
        self.popup_menu.add_command(label="Cut", command=self.edit_cut)
        self.popup_menu.add_command(label="Paste", command=self.edit_paste)
        self.popup_menu.add_command(label="Find", command=self.edit_find)
        self.popup_menu.add_separator()
    #    self.popup_menu.add_command(label="Help", command=self.help_open_help)
        self.window.bind("<Button-3>", self.popup_menu_event)

    def popup_menu_event(self, event):
        # find the x and y positions where the user clicked the right mouse button
        x_position_of_click = event.x_root
        y_position_of_click = event.y_root
        # post/place the pop menu where the user clicked.
        self.popup_menu.post(x_position_of_click, y_position_of_click)

    def edit_cut(event):
        pass

    def edit_copy(event):
        pass

    def edit_paste(event):
        pass

    def edit_find(event):
        pass


'''if __name__ == '__main__':
    window = Tk()
    window.title("Menu_Bar")
    window.geometry("400x300")
    Popup(window)
    window.mainloop()
'''