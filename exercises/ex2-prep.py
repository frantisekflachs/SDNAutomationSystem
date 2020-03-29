from sdn_controllers.floodlight import Floodlight

if __name__ == '__main__':

    sdnc = Floodlight()

    # enable firewall
    print(sdnc.firewallSetStatus('enable'))
    print(sdnc.firewallStatus())

    # clear firewall rules
    print(sdnc.firewallClearRules())