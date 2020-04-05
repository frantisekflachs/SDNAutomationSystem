from sdn_controllers.floodlight import Floodlight

if __name__ == '__main__':

    sdnc = Floodlight()

    # add rules for communication between host h1 and root (computer)
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.123.123.1/32"}))
    print(sdnc.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.1/32"}))

    # add rules for communication between host h2 and root (computer)
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.123.123.1/32"}))
    print(sdnc.firewallAddRule({"src-ip": "10.123.123.1/32", "dst-ip": "10.0.0.2/32"}))

    # allow ARP between host h1 and h3
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "dl-type": "ARP"}))
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "dl-type": "ARP"}))

    # allow ICMP between host h1 and h3
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "nw-proto": "ICMP"}))
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "nw-proto": "ICMP"}))

    # allow ICMP between host h2 and h3
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.2/32", "dst-ip": "10.0.0.3/32", "nw-proto": "ICMP"}))
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.2/32", "nw-proto": "ICMP"}))

    # allow HTTP protocol on port 80 from host h1 to h3 (server)
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.3/32", "nw-proto": "TCP", "tp-dst": "80", "action": "ALLOW"}))
    print(sdnc.firewallAddRule({"src-ip": "10.0.0.3/32", "dst-ip": "10.0.0.1/32", "nw-proto": "TCP", "tp-src": "80", "action": "ALLOW"}))


    print(sdnc.firewallListRules())

    flow1 = {
        'switch': "00:00:00:00:00:00:00:01",
        "name": "flow_mod_1",
        "cookie": "0",
        "priority": "32768",
        "in_port": "1",
        "active": "true",
        "actions": "output=controller"
    }

    print(sdnc.addFlow(flow1))