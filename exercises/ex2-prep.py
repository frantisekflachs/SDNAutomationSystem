import paramiko

from sdn_controllers.floodlight import Floodlight

if __name__ == '__main__':

    host = {"username": "user",
            "password": "user",
            "hostname": '10.0.0.3'}

    command = "python3.7 -m http.server --bind 10.0.0.3 80"

    sshClient = paramiko.SSHClient()
    sshClient.load_system_host_keys()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(**host, timeout=3)

    chan = sshClient.get_transport().open_session()
    chan.exec_command(command)
    response = chan.recv_exit_status()

    print(response)


    sdnc = Floodlight()

    # enable firewall
    print(sdnc.firewallSetStatus('enable'))
    print(sdnc.firewallStatus())

    # clear firewall rules
    print(sdnc.firewallClearRules())



