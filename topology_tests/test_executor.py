from time import sleep
import yaml

from sdn_controllers.floodlight import Floodlight
from topology_tests.network_tests.ping2_network_test import Ping2NetworkTest
from topology_tests.network_tests.ping_network_test import PingNetworkTest
from topology_tests.network_tests.wget_network_test import WgetNetworkTest


class TestExecutor:
    """Executor for implemented tests in the define topology"""

    def __init__(self, SDNController):
        self.sdnController = SDNController

        self.implementedTests = {
            'ping_network_test': PingNetworkTest(),
            'ping2_network_test': Ping2NetworkTest(),
            'wget_network_test': WgetNetworkTest()
        }

    def run(self, testsFromConfig):
        """Execute test by test and return all results"""

        try:
            testsResults = []

            for test in testsFromConfig:
                testNameParam = test.split()
                testName = testNameParam[0]
                testParams = testNameParam[1:]
                expectedResult = testNameParam[-1]

                # print(expectedResult)

                if testName not in self.implementedTests.keys():
                    testsResults.append(str(testName) + ': Test is not implemented.')
                else:
                    # wait for convergence of the network
                    sleep(5)

                    returnValue = self.implementedTests[testName].execute(testParams)
                    # testsResults.append(str(testName) + ': ' + str(returnValue))
                    testsResults.append('Test ' + str(testsFromConfig.index(test) + 1) + ' - ' + str(testName) + str(
                        ': OK' if (str(returnValue) == str(expectedResult)) else ': ---'))

            return testsResults
        except Exception as e:
            print("Something went wrong " + str(e))


if __name__ == "__main__":
    SDNController = Floodlight()
    te = TestExecutor(SDNController)

    stream = open('../topology_templates/topology5.yaml', 'r')
    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

    tt = loadedTopologyConfig["topologyTests"]

    print(te.run(tt))
