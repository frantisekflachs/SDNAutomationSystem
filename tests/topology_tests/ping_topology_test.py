from tests.topology_tests.network_test import NetworkTest
import os


class PingNetworkTest(NetworkTest):

    def execute(self, dstIP):
        response = os.system("ping -c 1 {}".format(dstIP))

        if response == 0:
            return True
        else:
            return False
