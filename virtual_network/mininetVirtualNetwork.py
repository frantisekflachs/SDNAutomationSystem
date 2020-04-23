import subprocess

from virtual_network.virtualNetwork import VirtualNetwork


class MininetVirtualTopology(VirtualNetwork):
    """Virtual topology Mininet"""

    def __init__(self, networkTemplate, xterm):
        self.networkTemplate = networkTemplate
        self.xterm = xterm

    def run(self):
        """Run Mininet topology"""

        try:

            params = ''
            params += str(self.networkTemplate)
            params += ' ' + str(self.xterm)

            print(params)

            subprocess.Popen(["gnome-terminal", "-e",
                              "bash -c \"sudo mn --clean && python3.7 "
                              "/home/user/PycharmProjects/SDNAutomationSystem/mininet_virtual_net_sshd.py {}; "
                              "/bin/bash -i\"".format(params)])
        except Exception as e:
            print("Something went wrong " + str(e))
