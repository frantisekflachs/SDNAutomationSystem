import subprocess

from virtual_network.virtualNetwork import VirtualNetwork


class MininetVirtualTopology(VirtualNetwork):
    """Virtual topology Mininet"""

    def __init__(self, networkTemplate, networkSetup):
        self.networkTemplate = networkTemplate
        self.networkSetup = networkSetup

    def run(self):
        """Run Mininet topology"""

        params = ''
        params += str(self.networkTemplate)

        for i in self.networkSetup:
            params += ' ' + str(i)

        print(params)

        subprocess.Popen(["gnome-terminal", "-e", "bash -c \"sudo mn --clean && python3.7 /home/user/PycharmProjects/SDNAutomationSystem/mininet_virtual_net_sshd.py {}; /bin/bash -i\"".format(params)])

        # os.system('gnome-terminal -- bash -c '
        #           '"mn --custom network_templates/{}.py --topo {} '
        #           '--controller=remote,ip=localhost,port=6653 '
        #           '--switch ovsk,protocols=OpenFlow10 '
        #           '&& bash"'.format(self.networkTemplate,
        #                             self.networkTemplate))
