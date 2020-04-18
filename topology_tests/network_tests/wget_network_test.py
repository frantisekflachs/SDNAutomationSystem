import paramiko

from topology_tests.network_tests.network_test import NetworkTest

class WgetNetworkTest(NetworkTest):

    def execute(self, params):
        """Execute Wget network test with parameters
        params[0]: host IP - host that will execute the command
        parames[1]: server IP - address that will be tried to wget something"""

        try:
            # print(params)
            srcIP = params[0]
            dstIP = params[1]

            host = {"username": "user",
                    "password": "user",
                    "hostname": srcIP}

            command = "wget -O – -t 1 --timeout=1 {}".format(dstIP)

            sshClient = paramiko.SSHClient()
            sshClient.load_system_host_keys()
            sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshClient.connect(**host, timeout=3)
            chan = sshClient.get_transport().open_session()
            chan.exec_command(command)
            response = chan.recv_exit_status()

            if response == 0:
                return True
            else:
                return False

        except Exception as e:
            print("Something went wrong " + str(e))
            return False