import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Frame
import tkinter as tk
import os

import yaml
import config


class ViewTemplates:
    """GUI for editing topology templates"""

    def __init__(self, parent):
        self.container = parent
        self.initialize()
        self.loadExistingTemplates()

    def initialize(self):
        """Init items in GUI"""

        # list existing topologies
        self.lblTopologyTemplates = Label(self.container, text='Topology templates')
        self.lblTopologyTemplates.pack()
        self.lblTopologyTemplates.place(x=20, y=20)

        self.frameTopologyTemplates = Frame(self.container)
        self.scrollTopologyTemplates = Scrollbar(self.frameTopologyTemplates)
        self.txtTopologyTemplates = Listbox(self.frameTopologyTemplates, width=37, height=36)
        self.scrollTopologyTemplates.pack(side=RIGHT, fill=tk.Y)
        self.txtTopologyTemplates.pack(side=LEFT, fill=tk.Y)
        self.scrollTopologyTemplates.config(command=self.txtTopologyTemplates.yview)
        self.txtTopologyTemplates.configure(yscrollcommand=self.scrollTopologyTemplates.set)
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

        self.txtTemplateName = Entry(self.container, width=30)
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
        self.btnSaveTemplate = tk.Button(self.container, text='Save template', width=20, command=self.saveTemplate)
        self.btnSaveTemplate.pack()
        self.btnSaveTemplate.place(x=990, y=750)

    def editTemplate(self):
        """Edit template button pressed"""

        try:
            self.txtTemplateName.config(state=NORMAL)
            self.txtTemplateName.delete(0, END)
            self.txtTemplateInfo.config(state=NORMAL)
            self.txtTemplateInfo.delete('1.0', END)
            self.txtTemplateSetting.delete('1.0', END)

            selTopo = self.txtTopologyTemplates.get(ACTIVE)

            entries = os.listdir(config.topologyTemplatesConfigPath)
            entries.sort()

            for entry in entries:
                if ("yaml" in entry) and ("topologyTemplate" not in entry):
                    stream = open(config.topologyTemplatesConfigPath + "/" + entry, 'r')
                    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

                    if entry == selTopo:
                        topologyDescription = loadedTopologyConfig["topologyDescription"]
                        topologyAuthor = loadedTopologyConfig["topologyAuthor"]
                        topologyVersion = loadedTopologyConfig["topologyVersion"]
                        topolofyOFVersion = loadedTopologyConfig["topolofyOFVersion"]
                        self.txtTemplateName.insert(0, entry)
                        self.txtTemplateName.config(state=DISABLED)

                        if not topologyDescription == None: self.txtTemplateInfo.insert(END, "Description: " + str(topologyDescription) + '\n')
                        if not topologyAuthor == None: self.txtTemplateInfo.insert(END, "Author: " + str(topologyAuthor) + '\n')
                        if not topologyVersion == None: self.txtTemplateInfo.insert(END, "Version: " + str(topologyVersion) + '\n')
                        if not topolofyOFVersion == None: self.txtTemplateInfo.insert(END, "OF Version: " + str(topolofyOFVersion) + '\n')

                        self.txtTemplateInfo.config(state=DISABLED)

                        f = open(config.topologyTemplatesConfigPath + "/" + entry, "r")
                        if f.mode == 'r':
                            content = f.read()
                            self.txtTemplateSetting.insert("1.0", content)
                        f.close()
                        break
        except Exception as e:
            print("Something went wrong " + str(e))
            self.txtTemplateInfo.insert("1.0", "Template error.")

    def deleteTemplate(self):
        """Delete template button pressed"""

        selTopo = self.txtTopologyTemplates.get(ACTIVE)

        try:
            MsgBox = messagebox.askquestion('Deleting template', 'Are you sure you want to delete ' + selTopo + ' template?',
                                               icon='warning')
            if MsgBox == 'yes':
                os.remove(config.topologyTemplatesConfigPath + '/' + selTopo)
                print("File " + selTopo + " deleted.")
                self.loadExistingTemplates()

        except Exception as e:
            print("Something went wrong " + str(e))
            print("Error while deleting file ", selTopo)
            self.txtTemplateInfo.insert("1.0", "Template error.")

    def loadDefaultTemplate(self):
        """Load default template from file to text fields in GUI"""

        try:

            self.txtTemplateName.config(state=NORMAL)
            self.txtTemplateName.delete(0, END)

            self.txtTemplateInfo.config(state=NORMAL)
            self.txtTemplateInfo.delete('1.0', END)

            self.txtTemplateSetting.delete('1.0', END)

            f = open(config.topologyTemplatesConfigPath + "/topologyTemplate.yaml", "r")
            if f.mode == 'r':
                content = f.read()
                self.txtTemplateSetting.insert("1.0", content)
            f.close()

            timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            self.txtTemplateName.insert(0, 'topology_' + timeNow)
            # self.txtTemplateName.insert('1.0', 'topo' + '\n')

        except Exception as e:
            print("Something went wrong " + str(e))

    def loadExistingTemplates(self):
        """Loading templates from system directory saved on the disk"""

        try:
            self.txtTopologyTemplates.delete(0, END)

            entries = os.listdir(config.topologyTemplatesConfigPath)
            entries.sort()

            for entry in entries:
                if ("yaml" in entry) and ("Template" not in entry):
                    self.txtTopologyTemplates.insert(END, entry)
        except Exception as e:
            print("Something went wrong " + str(e))

    def saveTemplate(self):
        """Save template created in GUI on the disk"""

        try:
            templateName = self.txtTemplateName.get()
            templateSetting = self.txtTemplateSetting.get('1.0', END)
            print(templateName)

            filename = ""
            if "yaml" in templateName:
                filename = config.topologyTemplatesConfigPath + "/" + str(templateName)
            else:
                filename = config.topologyTemplatesConfigPath + "/" + str(templateName) + ".yaml"

            f = open(filename, "w")
            f.write(templateSetting)
            f.flush()
            f.close()

            self.loadExistingTemplates()

        except Exception as e:
            print("Something went wrong " + str(e))

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