from tests.topology_tests.topology_test import TopologyTest
import os


class PingTopologyTest(TopologyTest):

    def execute(self, dstIP):
        response = os.system("ping -c 1 {}".format(dstIP))

        if response == 0:
            return True
        else:
            return False
