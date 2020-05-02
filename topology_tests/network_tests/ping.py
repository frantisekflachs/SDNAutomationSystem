from topology_tests.network_tests.network_test import NetworkTest
import paramiko


class Ping(NetworkTest):

    def execute(self, params):
        """Execute ping network test with parameters
        params[0]: repeat count
        params[1]: source IP - host that will execute the command
        parames[2]: destination IP - address that will be tried to ping"""

        try:
            repeat = params[0]
            srcIP = params[1]
            dstIP = params[2]

            # print(params)

            host = {"username": "user",
                    "password": "user",
                    "hostname": srcIP}

            command = "ping -c {} {}".format(repeat, dstIP)

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
