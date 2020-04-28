from topology_tests.network_tests.network_test import NetworkTest
import os
import paramiko


class NcTcp2NetworkTest(NetworkTest):

    def execute(self, testParams):
        """Execute ping network test with parameters
        testParams[0]: wait for communication
        testParams[1]: client IP address
        testParams[2]: server IP address
        testParams[3]: router port IP"""

        try:
            wait = testParams[0]
            clientIp = testParams[1]
            serverIp = testParams[2]
            routerPortIp = testParams[3]

            # print(params)

            host = {"username": "user",
                    "password": "user",
                    "hostname": routerPortIp}

            os.system('sudo rm -f /home/user/file.in')
            os.system('echo TCP data from IP: {} > /home/user/file.in'.format(clientIp))

            command = "sshpass -p {} ssh -o 'StrictHostKeyChecking no' -t {}@{} 'sudo nc -w {} {} 666 < /home/user/file.in'".format(host["password"],
                                                                                                      host["username"],
                                                                                                      clientIp, wait,
                                                                                                      serverIp)

            sshClient = paramiko.SSHClient()
            sshClient.load_system_host_keys()
            sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshClient.connect(**host, timeout=3)

            chan = sshClient.get_transport().open_session()
            chan.exec_command(command)
            response = chan.recv_exit_status()
            sshClient.close()

            print(response)

            if response == 0:
                return True
            else:
                return False

        except Exception as e:
            print("Something went wrong " + str(e))
            return False
