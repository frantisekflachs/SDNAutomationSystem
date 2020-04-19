from time import sleep

import config
from sdn_controllers.opendaylight import Opendaylight
from sdn_controllers.floodlight import Floodlight
from sdn_controllers.onos import Onos
from sdn_controllers.pox import Pox
from sdn_controllers.ryu import Ryu


class Topology4PostConfig:
    """Topology 4 post configuration"""

    def execute(self, sdnc):
        """Execute post configuration for topology 4"""

        try:
            # try 5 times to get state of SDN Controller, if not running or responding, return False
            for i in range(0, 5):

                if not sdnc.isRunning():
                    print(i)
                    if i == 1000:
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
            # enable firewall
            print(sdnc.firewallSetStatus('enable'))
            print(sdnc.firewallStatus())

            # clear firewall rules
            print(sdnc.firewallClearRules())

            # add rules for communication between host h1 and root (computer)
            print(sdnc.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.123.123.1/32"}))
            print(sdnc.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.1/32"}))

            # add rules for communication between host h2 and root (computer)
            print(sdnc.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.123.123.1/32"}))
            print(sdnc.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.2/32"}))
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def onosConfig(self):
        """Configuring Onos controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def opendaylightConfig(self):
        """Configuring OpenDaylight controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def poxConfig(self):
        """Configuring Pox controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False

    def ryuConfig(self):
        """Configuring Ryu controller after started for this example"""

        try:
            # DO SOME POST CONFIG
            return True
        except Exception as e:
            print("Something went wrong " + str(e))
            return False


if __name__ == "__main__":
    topo = Topology4PostConfig()
    topo.execute(config.implementedSDNControllers['Floodlight'])