import tkinter as tk
from tkinter import *
from tkinter import ttk
from pubsub import pub
import config
import datetime


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
        self.loadTopologyTemplates(config.implementedTopologyTemplates)
        self.loadImplementedSDNControllers(config.implementedSDNControllers)

    def initGUI(self):
        """Inicializing Graphical User Interface"""

        # menu
        menubar = Menu(self.container)
        menubar.add_command(label="Topology", command="")
        menubar.add_command(label="Templates", command="")
        menubar.add_command(label="Help", command="")
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

        # end topology button
        self.btnEndTopology = tk.Button(self.container, text='End topology', width=20, command=self.endTopology)
        self.btnEndTopology.pack()
        self.btnEndTopology.place(x=380, y=260)

        # open SDN Controller GUI button
        self.btnSDNControllerGui = tk.Button(self.container, text='Open SDN Controller GUI', width=20,
                                             command=self.openSDNControllerGui)
        self.btnSDNControllerGui.pack()
        self.btnSDNControllerGui.place(x=380, y=300)

        # test topology button
        self.btnTestTopology = tk.Button(self.container, text='Test topology', width=20, command=self.testTopology)
        self.btnTestTopology.pack()
        self.btnTestTopology.place(x=380, y=340)

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

    def loadTopologyTemplates(self, templates):
        """Load topology templates from path file"""

        for t in templates:
            self.lstTopologyTemplate.insert(END, t)

    def loadImplementedSDNControllers(self, controllers):
        """Load implemented controllers"""

        for c in controllers:
            self.cmbSDNController['values'] = (*self.cmbSDNController['values'], c)

    def loadImplementedTopologyTests(self, topologyTests):
        """Load implemented topology tests"""

        for tc in topologyTests:
            testNameParam = tc.split()
            testName = testNameParam[0]
            self.txtTopologyTests.insert(END, 'Test ' + str(topologyTests.index(tc) + 1) + ' - ' + str(testName) + ': --- \n')

    def getSelectedSDNController(self):
        """Returns name of selected controller"""

        return self.cmbSDNController.get()

    def getSelectedTopologyTemplate(self):
        """Return name of selected topology"""

        return self.lstTopologyTemplate.get(ACTIVE)

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
            print(timeNow + " " + data)

            # print to text field
            self.txtLogger.insert(END, timeNow + " " + data + '\n')

            # save to log file
            timeNow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            self.f.write(timeNow + " " + data + '\n')
            self.f.flush()

    def printTextTopologyTests(self, data):
        """Print text to text field with Tests Results"""

        self.txtTopologyTests.delete('1.0', END)

        for test in data:
            self.txtTopologyTests.insert(END, test + '\n')

    def runTopology(self):
        """Button run topology pressed"""

        pub.sendMessage("btnRunTopology_Pressed")

    def endTopology(self):
        """Button end topology pressed"""

        pub.sendMessage("btnEndTopology_Pressed")

    def openSDNControllerGui(self):
        """Show SDN Controller GUI"""

        pub.sendMessage("btnSDNControllerGui_Pressed")

    def testTopology(self):
        """Test configured topology"""

        pub.sendMessage("btnTestTopology_Pressed")


# test view
if __name__ == "__main__":
    root = tk.Tk()
    WIDTH = 600
    HEIGHT = 700
    root.geometry("%sx%s" % (WIDTH, HEIGHT))
    root.title("SDN automation system")
    view = View(root)

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

    print(view.getXTerm())
