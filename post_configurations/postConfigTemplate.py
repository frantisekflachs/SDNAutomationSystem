from time import sleep

from sdn_controllers.opendaylight import Opendaylight
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos
from sdn_controllers.pox import Pox
from sdn_controllers.ryu import Ryu


class PostConfigTemplate:
    """Topology post configuration template"""

    def execute(self, sdnc):
        """Execute post configuration"""

        try:
            # try 5 times to get state of SDN Controller, if not running or responding, return False
            for i in range(0, 5):

                if not sdnc.isRunning():
                    print(i)
                    if i == 5:
                        print('Controller ' + str(sdnc) + ' is not responding.')
                        return False
                    sleep(0.5)
                    continue

            print('Configuring Post Config for ' + str(sdnc))

            # loaded controller is Floodlight
            if isinstance(sdnc, Floodlight):
                # print('Floodlight')
                ret = self.floodlightConfig(sdnc)

            # loaded controller is Onos
            elif isinstance(sdnc, Onos):
                ret = self.onosConfig(sdnc)

            # loaded controller is Opendaylight
            elif isinstance(sdnc, Opendaylight):
                ret = self.opendaylightConfig(sdnc)

            # loaded controller is Pox
            elif isinstance(sdnc, Pox):
                ret = self.poxConfig(sdnc)

            # loaded controller is Ryu
            elif isinstance(sdnc, Ryu):
                ret = self.ryuConfig(sdnc)

            return ret

        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def floodlightConfig(self, sdnc):
        """Configuring Floodlight controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def onosConfig(self, sdnc):
        """Configuring Onos controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def opendaylightConfig(self, sdnc):
        """Configuring OpenDaylight controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def poxConfig(self, sdnc):
        """Configuring Pox controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def ryuConfig(self, sdnc):
        """Configuring Ryu controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False
