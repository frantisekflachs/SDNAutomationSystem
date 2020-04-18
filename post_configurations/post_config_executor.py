from time import sleep
import yaml

import config
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.sdnController import SDNController


class PostConfigExecutor:

    def __init__(self, SDNController):
        self.sdnController = SDNController
        #
        # self.implementedTests = {
        #     'ping_network_test': PingNetworkTest(),
        #     'wget_network_test': WgetNetworkTest()
        # }

    def run(self, postScriptsFromConfig):

        postConfigResults = []

        for script in postScriptsFromConfig:
            testNameParam = script.split()
            testName = testNameParam[0]
            testParams = testNameParam[1:]

            if testName not in self.implementedTests.keys():
                postConfigResults.append(str(testName) + ': Method is not implemented.')
            else:

                returnValue = self.implementedTests[testName].execute(testParams)


                postConfigResults.append(returnValue)

        return postConfigResults

if __name__ == "__main__":
    SDNController = Floodlight()
    te = PostConfigExecutor(SDNController)

    stream = open('../topology_templates/topology2.yaml', 'r')
    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

    tt = loadedTopologyConfig["topologyTests"]
    nt = loadedTopologyConfig["networkTemplate"]
    ns = loadedTopologyConfig['networkSetup']
    sdns = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(Floodlight)]]
    pc = loadedTopologyConfig['sdnControllersPostConfig']

    print(te.run(pc))
