from time import sleep

import config
from sdn_controllers.opendaylight import Opendaylight
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos
from sdn_controllers.pox import Pox
from sdn_controllers.ryu import Ryu


class Topology5PostConfig:
    """Topology 5 post configuration"""

    def execute(self, sdnc):
        """Execute post configuration for topology 5"""

        try:
            # try if sdnc is running for 90 sec
            for i in range(0, 90):
                if not sdnc.isRunning():
                    print("SDN Controller not running yet: " + str(i))
                    sleep(1)
                else:
                    break

            if not sdnc.isRunning():
                print('SDN Controller is not running.')
                return False
            else:
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


if __name__ == "__main__":
    topo = Topology5PostConfig()
    topo.execute(config.implementedSDNControllers['Floodlight'])