from topology_tests.topology_test import TopologyTest
from sdn_controllers.floodlight import Floodlight


class FwStatus(TopologyTest):
    """Testing for SDN Controller firewall status"""

    def execute(self, testParams):
        """ Execute the test for getting FW status from SDN Controller
        params: status that we are asking"""

        try:
            status = testParams[0]

            # print(testParams)

            sdnc = Floodlight()
            # get FW status from SDN controller
            currentStatus = sdnc.firewallStatus()
            # print(currentStatus['result'])
            if status in currentStatus['result']:
                return True
            else:
                return False

        except Exception as e:
            print("Something went wrong " + str(e))
            return False
