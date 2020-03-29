from sdn_controllers.sdnController import SDNController


class Topology2PostConfig:

    def __init__(self, SDNController):
        self.sdnc = SDNController

    def run(self):
        returnValues = []
        returnValues.append(self.sdnc.firewallSetStatus('disabled'))

        return returnValues
