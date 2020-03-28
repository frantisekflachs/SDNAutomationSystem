import subprocess

from topology_tests.network_tests.network_test import NetworkTest
import os
import paramiko


class PingNetworkTest(NetworkTest):

    def execute(self, params):
        """Execute ping network test witk parameters
        params[0]: repeat count
        params[1]: source IP - host that will execute the command
        parames[2]: destination IP - address that will be tried to ping"""

        try:
            # print(params)
            repeat = params[0]
            srcIP = params[1]
            dstIP = params[2]

            # response = os.system("ping -c {} {}".format(repeat, dstIP))

            host = {"username": "user",
                    "password": "user",
                    "hostname": srcIP}

            command = "ping -c {} {}".format(repeat, dstIP)

            sshClient = paramiko.SSHClient()
            sshClient.load_system_host_keys()
            sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshClient.connect(**host)

            chan = sshClient.get_transport().open_session()
            chan.exec_command(command)
            response = chan.recv_exit_status()
            # print(response)

            if response == 0:
                return True
            else:
                return False

        except:
            return False
