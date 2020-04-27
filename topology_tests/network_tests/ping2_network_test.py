from topology_tests.network_tests.network_test import NetworkTest
import paramiko


class Ping2NetworkTest(NetworkTest):

    def execute(self, testParams):
        """Execute ping network test with parameters
        testParams[0]: router IP from that tests will be created
        testParams[1]: repeat count
        testParams[2]: source IP - host that will execute the command
        testParams[3]: destination IP - address that will be tried to ping"""

        try:
            repeat = testParams[0]
            srcIP = testParams[1]
            dstIP = testParams[2]
            routerPortIp = testParams[3]

            # print(params)

            host = {"username": "user",
                    "password": "user",
                    "hostname": routerPortIp}

            command = "sshpass -p {} ssh -t {}@{} 'ping -c {} {}'".format(host["password"], host["username"], srcIP, repeat, dstIP)

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
