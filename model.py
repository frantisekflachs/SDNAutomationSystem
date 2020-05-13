import os
import subprocess

from topology_tests.test_executor import TestExecutor
from virtual_network.mininetVirtualNetwork import MininetVirtualTopology
import config
import yaml


class Model:
    """ Model for the MVC architecture. """

    def loadTopologyConfig(self, topologyTemplateConfigPath, SDNController):
        """Load topology from yaml config file
        topologyTemplateConfigPath: path where to find yaml config file
        SDNController: defined SDN Controller - config will be loaded only for this SDN Controller not others"""

        try:
            stream = open(topologyTemplateConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            tt = loadedTopologyConfig["topologyTests"]
            nt = loadedTopologyConfig["networkTemplate"]
            sdns = loadedTopologyConfig[
                config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(SDNController)]]
            pc = loadedTopologyConfig['sdnControllersPostConfig']
            return tt, nt, sdns, pc

        except Exception as e:
            print("Something went wrong " + str(e))

    def loadSDNCTopologyTemplate(self, topologyTemplateConfigPath):
        """Load SDNC defined in yaml config file
        topologyTemplateConfigPath: path where to find yaml config file"""

        try:
            stream = open(topologyTemplateConfigPath, 'r')
            loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

            implementedSDNC = config.implementedSDNControllersNames
            sdncInTopologyTemplate = []
            for implsdnc in implementedSDNC:
                try:
                    sdnc = loadedTopologyConfig[implsdnc]
                    sdncInTopologyTemplate.append(implsdnc)
                except Exception as e:
                    print("Something went wrong " + str(e))

            return sdncInTopologyTemplate

        except Exception as e:
            print("Something went wrong " + str(e))

    def runSDNController(self, SDNController, SDNControllerSetup):
        """Run SDN Controller
        SDNController: Implemented SDN Controllers in the system
        SDNControllerSetup: parameters for SDN Controller"""

        try:
            SDNController.run(SDNControllerSetup)
        except Exception as e:
            print("Something went wrong " + str(e))

    def runVirtualNetwork(self, networkTemplate, xterm):
        """Run Network Topology
        networkTemplate: pre-defined netwrok template
        xterm: True/False """

        try:
            mvt = MininetVirtualTopology(networkTemplate, xterm)
            mvt.run()
        except Exception as e:
            print("Something went wrong " + str(e))

    def runPostConfigScript(self, postConfigScript):
        """Run script after controller and virtual network is started
        postConfigScript: script name that is defined in topology template"""

        try:
            ret = postConfigScript.run()
            return ret
        except Exception as e:
            print("Something went wrong " + str(e))

    def showSDNControllerGui(self, SDNController):
        """Show SDN Controller GUI
        SDNController: run GUI for defined SDN Controller"""

        try:
            SDNController.showSDNControllerGui()
        except Exception as e:
            print("Something went wrong " + str(e))

    def testTopology(self, loadedSDNController, topologyTests):
        """Testing topology
        loadedSDNController: SDN Controller name from the view, that was loaded
        topologyTests: loaded tests from topology template"""

        try:
            testExecutor = TestExecutor(loadedSDNController)
            testsResults = testExecutor.run(topologyTests)
            return testsResults
        except Exception as e:
            print("Something went wrong " + str(e))

    def runSelfDefinedScript(self, scriptName):
        """Run self defined script
        scriptName: name of the scipt that will be executed"""

        try:
            proc = subprocess.Popen(["gnome-terminal", "-e",
                                     "bash -c \"sudo python3.7 {}/{}.py; /bin/bash -i\"".format(
                                         config.pathExercises, scriptName[:-1])])
        except Exception as e:
            print("Something went wrong " + str(e))

    def endTopology(self):
        """End topology that could contain SDN Controllers and virtual instances from virtul network"""

        # kill all implemented SDN Controllers
        implSDNControllers = config.implementedSDNControllersNames
        for sdnc in implSDNControllers:
            try:
                print('SDN Controller ' + sdnc.lower() + ' exiting')
                os.system("sudo kill $(ps aux | grep '" + sdnc.lower() + "' | awk '{print $2}')")
            except Exception as e:
                print("Something went wrong " + str(e))

        # kill processes controller
        try:
            os.system("sudo killall controller")
        except Exception as e:
            print("Something went wrong " + str(e))

        # clean Mininet
        try:
            print('Mininet exiting and cleaning')
            os.system("sudo kill $(ps aux | grep 'sshd' | awk '{print $2}')")
            os.system("sudo kill $(ps aux | grep 'xterm' | awk '{print $2}')")
            os.system("service sshd restart")
            os.system("sudo mn --clean")
        except Exception as e:
            print("Something went wrong " + str(e))
