from sdn_controllers.opendaylight import Opendaylight
from tests.topology_tests.ping_topology_test import PingTopologyTest
import config
import yaml


class TestExecutor:

    def __init__(self, SDNController):
        self.sdnController = SDNController

        self.implementedTests = {
            'ping_topology_test': PingTopologyTest()
        }

    def run(self, testsFromConfig):

        testsResults = {}

        for test in testsFromConfig:
            testNameParam = test.split()
            testName = testNameParam[0]
            testParam = testNameParam[1]

            if testName not in self.implementedTests.keys():
                testsResults[testName] = 'Test is not implemented.'
                # print('### Test {} is not implemented.'.format(testName))
            else:
                returnValue = self.implementedTests[testName].execute(testParam)
                testsResults[testName] = returnValue
                # print('### {} with parameters: {} - {}'.format(testName, testParam, returnValue))

        return testsResults

# if __name__ == "__main__":
    # od = Opendaylight()
    # te = TestExecutor(od)
    #
    # stream = open("../topology_templates_config/topology1.yaml", 'r')
    # loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)
    #
    # config.topologyVersion = loadedTopologyConfig["topologyVersion"]
    # config.topologyIP = loadedTopologyConfig["topologyIP"]
    # config.tests = loadedTopologyConfig["tests"]
    #
    # te.run(config.tests)

