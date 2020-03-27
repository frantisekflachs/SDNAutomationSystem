import subprocess

from networkTopology.virtualTopology.virtualTopology import VirtualTopology
import os


class MininetVirtualTopology(VirtualTopology):
    """Virtual topology Mininet"""

    def __init__(self, networkTemplate, networkSetup):
        self.networkTemplate = networkTemplate
        self.networkSetup = networkSetup

    def run(self):
        """Run Mininet topology"""

        if not self.networkSetup:
            os.system('gnome-terminal -- bash -c '
                      '"mn --custom network_templates/{}.py --topo {} '
                      '--controller=remote,ip=localhost,port=6653 '
                      '--switch ovsk,protocols=OpenFlow10 '
                      '&& bash"'.format(self.networkTemplate,
                                        self.networkTemplate))

        else:
            runOptions = ''
            for switch in self.networkSetup:
                runOptions += ' ' + switch

            print(runOptions)

            os.system('gnome-terminal -- bash -c "mn{} --custom network_templates/{}.py --topo {} && bash"'
                      .format(runOptions, self.networkTemplate, self.networkTemplate))

    def run2(self):
        """Create network"""
        # os.system('gnome-terminal -- bash -c "python3.7 /home/user/PycharmProjects/SDNAutomationSystem/sshd.py && bash"')

        proc = subprocess.Popen(["gnome-terminal", "-e",
                                 "bash -c \"python3.7 /home/user/PycharmProjects/SDNAutomationSystem/sshd.py; /bin/bash -i\""])
        print(proc)
