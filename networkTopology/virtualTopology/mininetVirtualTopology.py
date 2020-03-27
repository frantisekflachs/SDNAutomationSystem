import subprocess

from networkTopology.virtualTopology.virtualTopology import VirtualTopology
import os


class MininetVirtualTopology(VirtualTopology):
    """Virtual topology Mininet"""

    def __init__(self, topologyTemplate, topologyIP, xTermEnable, OFVersion, SDNControllerIP):
        self.topologyTemplate = topologyTemplate
        self.topologyIP = topologyIP
        self.xTermEnable = xTermEnable
        self.OFVersion = OFVersion
        self.SDNControllerIP = SDNControllerIP

    def run(self):
        """Run Mininet topology"""

        if self.xTermEnable:
            os.system('gnome-terminal -- bash -c '
                      '"mn -x --custom topologyTemplates/{}.py --topo {} '
                      '-i {} --controller=remote,ip={},port=6653 '
                      '--switch ovsk,protocols=OpenFlow{} '
                      '&& bash"'.format(self.topologyTemplate,
                                        self.topologyTemplate,
                                        self.topologyIP,
                                        self.SDNControllerIP,
                                        self.OFVersion))

        else:
            os.system('gnome-terminal -- bash -c '
                      '"mn --custom topologyTemplates/{}.py --topo {} '
                      '-i {} --controller=remote,ip={},port=6653 '
                      '--switch ovsk,protocols=OpenFlow{} '
                      '&& bash"'.format(self.topologyTemplate,
                                        self.topologyTemplate,
                                        self.topologyIP,
                                        self.SDNControllerIP,
                                        self.OFVersion))

    def run2(self):
        """Create network"""
        # os.system('gnome-terminal -- bash -c "python3.7 /home/user/PycharmProjects/SDNAutomationSystem/sshd.py && bash"')

        proc = subprocess.Popen(["gnome-terminal", "-e", "bash -c \"python3.7 /home/user/PycharmProjects/SDNAutomationSystem/sshd.py; /bin/bash -i\""])
        print(proc)