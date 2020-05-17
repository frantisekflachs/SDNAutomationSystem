from topology_tests.network_tests.network_test import NetworkTest
import os


class OvsFlow(NetworkTest):

    def execute(self, params):
        """Execute ping network test with parameters
        params[0]: switch name
        params[1]: OpenFlow version (11, 13)
        params[2:]: match piece of OpenFlow rule definitions"""

        try:
            switchName = params[0]
            OfVersion = params[1]
            flowMatch = params[2:]

            commandOutput = os.popen('sudo ovs-ofctl -O OpenFlow{} dump-flows {}'.format(OfVersion, switchName))
            switchRules = commandOutput.read()

            match = False
            for flow in flowMatch:
                match = flow in switchRules
            return match

        except Exception as e:
            print("Something went wrong " + str(e))
            return False
