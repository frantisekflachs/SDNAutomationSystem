from time import sleep
import yaml

from sdn_controllers.floodlight import Floodlight
from topology_tests.controller_tests.acl_rule import AclRule
from topology_tests.controller_tests.flow_rule import FlowRule
from topology_tests.controller_tests.fw_rule import FwRule
from topology_tests.controller_tests.fw_status import FwStatus
from topology_tests.controller_tests.sdn_controller_test import SDNControllerTest
from topology_tests.network_tests.nc_tcp_2 import NcTcp2
from topology_tests.network_tests.nc_udp_2 import NcUdp2
from topology_tests.network_tests.network_test import NetworkTest
from topology_tests.network_tests.ovs_flow import OvsFlow
from topology_tests.network_tests.ping2 import Ping2
from topology_tests.network_tests.ping import Ping
from topology_tests.network_tests.wget import Wget


class TestExecutor:
    """Executor for implemented tests in the define topology"""

    def __init__(self, SDNController):
        self.sdnController = SDNController

        self.implementedTests = {
            # Network tests
            'ping': Ping(),
            'ping2': Ping2(),
            'wget': Wget(),
            'nc_tcp_2': NcTcp2(),
            'nc_udp_2': NcUdp2(),
            'ovs_flow': OvsFlow(),

            #SDN Controller tests
            'acl_rule': AclRule(),
            'fw_status': FwStatus(),
            'fw_rule': FwRule(),
            'flow_rule': FlowRule(),
        }

    def run(self, testsFromConfig):
        """Execute test by test and return all results"""

        try:
            testsResults = []

            for test in testsFromConfig:
                testNameParam = test.split()
                testName = testNameParam[0]
                testParams = testNameParam[1:-1]
                expectedResult = testNameParam[-1]

                # print(expectedResult)

                if testName not in self.implementedTests.keys():
                    testsResults.append(str(testName) + ': Test is not implemented.')
                else:
                    # wait for convergence of the network
                    sleep(5)

                    if isinstance(self.implementedTests[testName], SDNControllerTest):
                        # print('Instance of SDNC test')
                        returnValue = self.implementedTests[testName].execute(testParams, self.sdnController)
                        testsResults.append('Test ' + str(testsFromConfig.index(test) + 1) + ' - ' + str(testName) + str(
                            ': OK' if (str(returnValue) == str(expectedResult)) else ': ---'))
                        print(testsResults[-1])

                    if isinstance(self.implementedTests[testName], NetworkTest):
                        # print('Instance of Network test')
                        returnValue = self.implementedTests[testName].execute(testParams)
                        testsResults.append('Test ' + str(testsFromConfig.index(test) + 1) + ' - ' + str(testName) + str(
                            ': OK' if (str(returnValue) == str(expectedResult)) else ': ---'))
                        print(testsResults[-1])

            return testsResults
        except Exception as e:
            print("Something went wrong " + str(e))


if __name__ == "__main__":
    SDNController = Floodlight()
    te = TestExecutor(SDNController)

    stream = open('../topology_templates/topology3.yaml', 'r')
    loadedTopologyConfig = yaml.load(stream, Loader=yaml.FullLoader)

    tt = loadedTopologyConfig["topologyTests"]

    print(te.run(tt))
