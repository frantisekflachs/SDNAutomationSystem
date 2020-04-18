from sdn_controllers.floodlight import Floodlight

if __name__ == '__main__':

    sdnc = Floodlight()

    # print(sdnc.firewallClearRules())

    print(sdnc.firewallAddRule({"dl-type": "ARP"}))

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
