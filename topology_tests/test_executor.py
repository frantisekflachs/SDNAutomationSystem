import yaml

import config
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.opendaylight import Opendaylight
from topology_tests.network_tests.ping_network_test import PingNetworkTest
from topology_tests.network_tests.wget_network_test import WgetNetworkTest


class TestExecutor:

    def __init__(self, SDNController):
        self.sdnController = SDNController

        self.implementedTests = {
            'ping_network_test': PingNetworkTest(),
            'wget_network_test': WgetNetworkTest()
        }

    def run(self, testsFromConfig):

        testsResults = []

        for test in testsFromConfig:
            testNameParam = test.split()
            testName = testNameParam[0]
            testParams = testNameParam[1:]

            if testName not in self.implementedTests.keys():
                testsResults.append(str(testName) + ': Test is not implemented.')
            else:
                returnValue = self.implementedTests[testName].execute(testParams)
                testsResults.append(str(testName) + ': ' + str(returnValue))

        return testsResults

if __name__ == "__main__":
    SDNController = Floodlight()
    te = TestExecutor(SDNController)

    stream = open('../topology_templates_config/topology1.yaml', 'r')
    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

    tt = loadedTopologyConfig["topologyTests"]
    nt = loadedTopologyConfig["networkTemplate"]
    ns = loadedTopologyConfig['networkSetup']
    sdns = loadedTopologyConfig[config.implementedSDNControllersNames[config.implementedSDNControllersClasses.index(Floodlight)]]

    print(te.run(tt))

