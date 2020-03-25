from tkinter import Tk

from controller import Controller
from view import View
from model import Model

if __name__ == '__main__':
    root = Tk()
    model = Model()
    view = View(root)

    SDNAutomationSystem = Controller(model, view, root)

    # print('Application starting...')
    SDNAutomationSystem.view.printText('SDN Automation System is running.')

    WIDTH = 600
    HEIGHT = 700
    root.geometry("%sx%s" % (WIDTH, HEIGHT))
    root.title("SDN Automation System")
    root.resizable(width=False, height=False)

    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int((root.winfo_screenwidth() - windowWidth) / 2.5)
    positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.mainloop()
