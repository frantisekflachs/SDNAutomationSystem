from tkinter import Tk

from controller import Controller
from view import View
from model import Model

"""Main class for start up the SDN Automation System.
It's provided by GUI, where you can choose topology template and SDN Controler.
Starting si divided by only SDN Controller, Virtual network or whole topology together
System is provided by automated testing, tests are loaded after starting whole topology or only some part of it."""

if __name__ == '__main__':

    try:
        root = Tk()
        model = Model()
        view = View(root)

        SDNAutomationSystem = Controller(model, view, root)

        # print('Application starting...')
        SDNAutomationSystem.view.printTextLog('SDN Automation System is running.')

        WIDTH = 600
        HEIGHT = 700
        root.geometry("%sx%s" % (WIDTH, HEIGHT))
        root.title("SDN Automation System")
        root.resizable(width=False, height=False)

        # Gets the requested values of the height and widht.
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int((root.winfo_screenwidth() - windowWidth) / 2.5)
        positionDown = int(root.winfo_screenheight() / 5 - windowHeight / 2)

        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))
        root.mainloop()

        SDNAutomationSystem.endTopology()
        print('SDN Automation System has ended.')
    except Exception as e:
        print("Something went wrong " + str(e))
