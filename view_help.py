from tkinter import *
from tkinter.ttk import Frame
import tkinter as tk

import config


class ViewHelp:
    """HELP GUI frame with README file data info"""

    def __init__(self, parent):
        self.container = parent
        self.initialize()

        self.loadHelpData()

    def initialize(self):
        """ GUI init"""

        self.frameHelp = Frame(self.container)
        self.scrollHelp = Scrollbar(self.frameHelp)
        self.txtHelp = Text(self.frameHelp, width=85, height=46)
        self.scrollHelp.pack(side=RIGHT, fill=tk.Y)
        self.txtHelp.pack(side=LEFT, fill=tk.Y)
        self.scrollHelp.config(command=self.txtHelp.yview)
        self.txtHelp.configure(yscrollcommand=self.scrollHelp.set)
        self.frameHelp.place(x=0, y=0)

    def loadHelpData(self):
        """Load data from README file and display them."""

        try:
            f = open(config.readme, "r")
            if f.mode == 'r':
                content = f.read()
                self.txtHelp.insert("1.0", content)
            f.close()
        except Exception as e:
            print("Something went wrong " + str(e))


if __name__ == "__main__":

    root = tk.Tk()
    WIDTH = 700
    HEIGHT = 790
    root.geometry("%sx%s" % (WIDTH, HEIGHT))
    root.title("Help")
    view = ViewHelp(root)

    root.resizable(width=False, height=False)

    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int((root.winfo_screenwidth() - windowWidth) / 2.8)
    positionDown = int(root.winfo_screenheight() / 5 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    root.mainloop()