import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

import yaml
from pubsub import pub
import datetime

import config
from view_help import ViewHelp
from view_templates import ViewTemplates


class View:
    """ View for the MVC architecture. """

    def __init__(self, parent):
        # initialize variables
        self.container = parent

        # XTerm for hosts enable
        self.hostsXTerm = tk.BooleanVar()

        # init items in GUI
        self.initGUI()

        # file reader for logs
        self.f = self.logInit(config.logsPath)

        # load methods
        self.loadTopologyTemplates()
        self.loadImplementedSDNControllers(config.implementedSDNControllers)

    def initGUI(self):
        """Inicializing Graphical User Interface"""

        # menu
        menubar = Menu(self.container)
        menubar.add_command(label="Topology", command=self.loadTopologyTemplates)
        menubar.add_command(label="Templates", command=self.openTemplatesView)
        menubar.add_command(label="Help", command=self.openHelpView)
        self.container.config(menu=menubar)

        # list topology template
        self.frameTopologyTemplate = Frame(self.container)
        self.lstTopologyTemplateScroll = Scrollbar(self.frameTopologyTemplate)
        self.lstTopologyTemplate = Listbox(self.frameTopologyTemplate, width=68)
        self.lstTopologyTemplateScroll.pack(side=RIGHT, fill=tk.Y)
        self.lstTopologyTemplate.pack(side=LEFT, fill=tk.Y)
        self.lstTopologyTemplateScroll.config(command=self.lstTopologyTemplate.yview)
        self.lstTopologyTemplate.configure(yscrollcommand=self.lstTopologyTemplateScroll.set)
        self.frameTopologyTemplate.place(x=20, y=20)

        # sdn controller
        self.lblSDNController = Label(self.container, text='SDN Controller')
        self.lblSDNController.pack()
        self.lblSDNController.place(x=20, y=220)
        self.cmbSDNController = ttk.Combobox(self.container)
        self.cmbSDNController.pack()
        self.cmbSDNController.place(x=150, y=220)

        # Run with XTerm for all hosts
        self.hostsXTerm.set(False)
        self.chbtnXTerm = Checkbutton(self.container, text='run all hosts with XTerm', variable=self.hostsXTerm,
                                      onvalue=True, offvalue=False)
        self.chbtnXTerm.pack()
        self.chbtnXTerm.place(x=20, y=260)

        # list topology tests
        self.lblTopologyTests = Label(self.container, text='Topology tests')
        self.lblTopologyTests.pack()
        self.lblTopologyTests.place(x=20, y=300)

        self.frameTopologyTests= Frame(self.container)
        self.txtTopologyTestsScroll = Scrollbar(self.frameTopologyTests)
        self.txtTopologyTests = Text(self.frameTopologyTests, width=37, height=12)
        self.txtTopologyTestsScroll.pack(side=RIGHT, fill=tk.Y)
        self.txtTopologyTests.pack(side=LEFT, fill=tk.Y)
        self.txtTopologyTestsScroll.config(command=self.txtTopologyTests.yview)
        self.txtTopologyTests.configure(yscrollcommand=self.txtTopologyTestsScroll.set)
        self.frameTopologyTests.place(x=20, y=320)

        # run topology button
        self.btnRunTopology = tk.Button(self.container, text='Run topology', width=20, command=self.runTopology)
        self.btnRunTopology.pack()
        self.btnRunTopology.place(x=380, y=220)

        # run SDN Controller button
        self.btnRunSDNController = tk.Button(self.container, text='Run SDN Controller', width=20, command=self.runSDNController)
        self.btnRunSDNController.pack()
        self.btnRunSDNController.place(x=380, y=260)

        # run Virtual Network button
        self.btnRunVirtualNetwork = tk.Button(self.container, text='Run virtual network', width=20, command=self.runVirtualNetwork)
        self.btnRunVirtualNetwork.pack()
        self.btnRunVirtualNetwork.place(x=380, y=300)

        # end topology button
        self.btnEndTopology = tk.Button(self.container, text='End topology', width=20, command=self.endTopology)
        self.btnEndTopology.pack()
        self.btnEndTopology.place(x=380, y=340)

        # open SDN Controller GUI button
        self.btnSDNControllerGui = tk.Button(self.container, text='Open SDN Controller GUI', width=20,
                                             command=self.openSDNControllerGui)
        self.btnSDNControllerGui.pack()
        self.btnSDNControllerGui.place(x=380, y=380)

        # run script
        self.txtScriptName = Text(self.container, height=1, width=23)
        self.txtScriptName.pack()
        self.txtScriptName.place(x=380, y=430)
        self.txtScriptName.insert('1.0', 'exampleScript')

        self.btnRunScript = tk.Button(self.container, text='Run script', width=20,
                                             command=self.runScript)
        self.btnRunScript.pack()
        self.btnRunScript.place(x=380, y=460)

        # test topology button
        self.btnTestTopology = tk.Button(self.container, text='Test topology', width=20, command=self.testTopology)
        self.btnTestTopology.pack()
        self.btnTestTopology.place(x=380, y=500)

        # log panel
        self.frameLog = Frame(self.container)
        self.txtLoggerScroll = Scrollbar(self.frameLog)
        self.txtLogger = Text(self.frameLog, height=8)
        self.txtLoggerScroll.pack(side=RIGHT, fill=tk.Y)
        self.txtLogger.pack(side=LEFT, fill=tk.Y)
        self.txtLoggerScroll.config(command=self.txtLogger.yview)
        self.txtLogger.configure(yscrollcommand=self.txtLoggerScroll.set)
        self.frameLog.pack(side=BOTTOM)

    def logInit(self, path):
        """Init file reader for logs"""

        timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        f = open(path + "/" + timeNow + ".txt", "a")
        return f

    def loadTopologyTemplates(self):
        """Load topology templates from path file"""

        print("updated")

        try:
            self.lstTopologyTemplate.delete(0, END)
            entries = os.listdir(config.topologyTemplatesConfigPath)
            entries.sort()

            for entry in entries:
                if ("yaml" in entry) and ("topologyTemplate" not in entry):
                    stream = open(config.topologyTemplatesConfigPath + "/" + entry, 'r')
                    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)
                    topologyDescription = loadedTopologyConfig["topologyDescription"]
                    self.lstTopologyTemplate.insert(END, entry + ': ' + topologyDescription)
        except Exception as e:
            print("Something went wrong " + str(e))

    def loadImplementedSDNControllers(self, controllers):
        """Load implemented controllers"""

        for c in controllers:
            self.cmbSDNController['values'] = (*self.cmbSDNController['values'], c)

    def loadImplementedTopologyTests(self, topologyTests):
        """Load implemented topology tests"""

        self.txtTopologyTests.delete('1.0', END)

        for tc in topologyTests:
            testNameParam = tc.split()
            testName = testNameParam[0]
            self.txtTopologyTests.insert(END, 'Test ' + str(topologyTests.index(tc) + 1) + ' - ' + str(testName) + ': --- \n')

    def getSelectedSDNController(self):
        """Returns name of selected controller"""

        return self.cmbSDNController.get()

    def getSelectedTopologyTemplate(self):
        """Return name of selected topology"""

        activeTopoTemplate = self.lstTopologyTemplate.get(ACTIVE).split(":")
        # return only topo "name.yaml"
        return activeTopoTemplate[0]

    def getXTerm(self):
        """Return if run with XTerm for all hosts"""

        return self.hostsXTerm.get()

    def printTextLog(self, data):
        """Print text to console, file and to log window.
        data: data to write to console, GUI and to file"""

        if type(data) is dict:
            # print('is dictionary')

            for test, testResult in data.items():
                timeNow = datetime.datetime.now().strftime("%H:%M:%S")

                # print to console
                print('{} {}: {}'.format(timeNow, test, testResult))

                # print to text field
                self.txtLogger.insert(END, '{} {}: {} \n'.format(timeNow, test, testResult))
                self.txtLogger.see("end")

                # save to log file
                timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                self.f.write('{} {}: {} \n'.format(timeNow, test, testResult))
                self.f.flush()

        elif type(data) is list:
            # print('is list')

            for testResult in data:
                timeNow = datetime.datetime.now().strftime("%H:%M:%S")

                # print to console
                print('{} {}'.format(timeNow, testResult))

                # print to text field
                self.txtLogger.insert(END, '{} {} \n'.format(timeNow, testResult))
                self.txtLogger.see("end")

                # save to log file
                timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                self.f.write('{} {} \n'.format(timeNow, testResult))
                self.f.flush()

        else:
            timeNow = datetime.datetime.now().strftime("%H:%M:%S")

            # print to console
            print(timeNow + " " + str(data))

            # print to text field
            self.txtLogger.insert(END, timeNow + " " + str(data) + '\n')
            self.txtLogger.see("end")

            # save to log file
            timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            self.f.write(timeNow + " " + str(data) + '\n')
            self.f.flush()

    def printTextTopologyTests(self, data):
        """Print text to text field with Tests Results"""

        self.txtTopologyTests.delete('1.0', END)

        for test in data:
            self.txtTopologyTests.insert(END, test + '\n')

    def openTemplatesView(self):
        """Open GUI for editing templates"""
        parrent2 = Toplevel(self.container)


        WIDTH = 1200
        HEIGHT = 800
        parrent2.geometry("%sx%s" % (WIDTH, HEIGHT))
        parrent2.title("Edit topology templates")
        templatesGUI = ViewTemplates(parrent2)

        parrent2.resizable(width=False, height=False)

        # Gets the requested values of the height and widht.
        windowWidth = parrent2.winfo_reqwidth()
        windowHeight = parrent2.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int((parrent2.winfo_screenwidth() - windowWidth) / 4.5)
        positionDown = int(parrent2.winfo_screenheight() / 5 - windowHeight / 2)

        # Positions the window in the center of the page.
        parrent2.geometry("+{}+{}".format(positionRight, positionDown))

    def openHelpView(self):
        """Open GUI for help"""
        parrent3 = Toplevel(self.container)


        WIDTH = 700
        HEIGHT = 790
        parrent3.geometry("%sx%s" % (WIDTH, HEIGHT))
        parrent3.title("Help")
        templatesGUI = ViewHelp(parrent3)

        parrent3.resizable(width=False, height=False)

        # Gets the requested values of the height and widht.
        windowWidth = parrent3.winfo_reqwidth()
        windowHeight = parrent3.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int((parrent3.winfo_screenwidth() - windowWidth) / 2.8)
        positionDown = int(parrent3.winfo_screenheight() / 5 - windowHeight / 2)

        # Positions the window in the center of the page.
        parrent3.geometry("+{}+{}".format(positionRight, positionDown))

    def getScriptName(self):
        """Return self defined script name"""

        return self.txtScriptName.get("1.0", END)

    def runTopology(self):
        """Button run topology pressed"""

        pub.sendMessage("btnRunTopology_Pressed")

    def runSDNController(self):
        """Button run SDN Controller pressed"""

        pub.sendMessage("btnRunSDNController_Pressed")

    def runVirtualNetwork(self):
        """Button run virtul network pressed"""

        pub.sendMessage("btnRunVirtualNetwork_Pressed")

    def endTopology(self):
        """Button end topology pressed"""

        pub.sendMessage("btnEndTopology_Pressed")

    def openSDNControllerGui(self):
        """Show SDN Controller GUI"""

        pub.sendMessage("btnSDNControllerGui_Pressed")

    def runScript(self):
        """Run created python script"""

        pub.sendMessage("btnRunScript_Pressed")

    def testTopology(self):
        """Test configured topology"""

        pub.sendMessage("btnTestTopology_Pressed")


# test view
if __name__ == "__main__":
    root = tk.Tk()
    WIDTH = 600
    HEIGHT = 700
    root.geometry("%sx%s" % (WIDTH, HEIGHT))
    root.title("SDN Automation System")
    view = View(root)

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
