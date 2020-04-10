from tkinter import *
from tkinter.ttk import Frame
import tkinter as tk


class ViewTemplates():

    def __init__(self, parent):
        self.container = parent
        self.initialize()

    def initialize(self):

        # list existing topologies
        self.lblTopologyTemplates = Label(self.container, text='Topology templates')
        self.lblTopologyTemplates.pack()
        self.lblTopologyTemplates.place(x=20, y=20)

        self.frameTopologyTemplates = Frame(self.container)
        self.txtTopologyTemplates = Scrollbar(self.frameTopologyTemplates)
        self.txtTopologyTests = Text(self.frameTopologyTemplates, width=37, height=38)
        self.txtTopologyTemplates.pack(side=RIGHT, fill=tk.Y)
        self.txtTopologyTests.pack(side=LEFT, fill=tk.Y)
        self.txtTopologyTemplates.config(command=self.txtTopologyTests.yview)
        self.txtTopologyTests.configure(yscrollcommand=self.txtTopologyTemplates.set)
        self.frameTopologyTemplates.place(x=20, y=40)

        # button edit template
        self.btnEditTemplate = tk.Button(self.container, text='Edit template', width=36, command=self.editTemplate)
        self.btnEditTemplate.pack()
        self.btnEditTemplate.place(x=20, y=710)

        # button delete template
        self.btnDeleteTemplate = tk.Button(self.container, text='Delete template', width=36, command=self.deleteTemplate)
        self.btnDeleteTemplate.pack()
        self.btnDeleteTemplate.place(x=20, y=750)

        # template name
        self.lblTemplateName = Label(self.container, text='Template name')
        self.lblTemplateName.pack()
        self.lblTemplateName.place(x=400, y=20)

        self.txtTemplateName = Text(self.container, height=1, width=23)
        self.txtTemplateName.pack()
        self.txtTemplateName.place(x=550, y=20)

        # template info
        self.lblTemplateInfo= Label(self.container, text='Template info')
        self.lblTemplateInfo.pack()
        self.lblTemplateInfo.place(x=400, y=60)

        self.frameTemplateInfo = Frame(self.container)
        self.scrollTemplateInfo = Scrollbar(self.frameTemplateInfo)
        self.txtTemplateInfo = Text(self.frameTemplateInfo, width=95, height=6)
        self.scrollTemplateInfo.pack(side=RIGHT, fill=tk.Y)
        self.txtTemplateInfo.pack(side=LEFT, fill=tk.Y)
        self.scrollTemplateInfo.config(command=self.txtTemplateInfo.yview)
        self.txtTemplateInfo.configure(yscrollcommand=self.scrollTemplateInfo.set)
        self.frameTemplateInfo.place(x=400, y=80)

        # template settings
        self.lblTemplateSetting= Label(self.container, text='Template setting')
        self.lblTemplateSetting.pack()
        self.lblTemplateSetting.place(x=400, y=200)

        self.frameTemplateSetting = Frame(self.container)
        self.scrollTemplateSetting = Scrollbar(self.frameTemplateSetting)
        self.txtTemplateSetting = Text(self.frameTemplateSetting, width=95, height=30)
        self.scrollTemplateSetting.pack(side=RIGHT, fill=tk.Y)
        self.txtTemplateSetting.pack(side=LEFT, fill=tk.Y)
        self.scrollTemplateSetting.config(command=self.txtTemplateSetting.yview)
        self.txtTemplateSetting.configure(yscrollcommand=self.scrollTemplateSetting.set)
        self.frameTemplateSetting.place(x=400, y=220)

        # button load defaults
        self.btnLoadDefaultTemplate = tk.Button(self.container, text='Load default template', width=20, command=self.loadDefaultTemplate)
        self.btnLoadDefaultTemplate.pack()
        self.btnLoadDefaultTemplate.place(x=780, y=750)

        # button save template
        self.btnSaveTemplate = tk.Button(self.container, text='Save template', width=20, command=self.loadDefaultTemplate)
        self.btnSaveTemplate.pack()
        self.btnSaveTemplate.place(x=990, y=750)


    def editTemplate(self):
        pass

    def deleteTemplate(self):
        pass

    def loadDefaultTemplate(self):
        pass

if __name__ == "__main__":

    root = tk.Tk()
    WIDTH = 1200
    HEIGHT = 800
    root.geometry("%sx%s" % (WIDTH, HEIGHT))
    root.title("Edit topology templates")
    view = ViewTemplates(root)

    root.resizable(width=False, height=False)

    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int((root.winfo_screenwidth() - windowWidth) / 4.5)
    positionDown = int(root.winfo_screenheight() / 5 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    root.mainloop()