import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from sdn_controllers.floodlight import Floodlight

if __name__ == '__main__':

    try:
        sdnc = Floodlight()

        print(sdnc.clearAclRules())
        print(sdnc.listAclRules())

        print('TASK 1 - ICMP')
        # TASK 1 - ICMP
        rule1 = {
            'src-ip': '192.168.0.100/32',
            'dst-ip': '172.16.0.100/32',
            'nw-proto': 'ICMP',
            'action': 'ALLOW'
        }
        rule2 = {
            'src-ip': '10.0.0.100/32',
            'dst-ip': '172.16.0.100/32',
            'nw-proto': 'ICMP',
            'action': 'ALLOW'
        }
        rule3 = {
            'dst-ip': '172.16.0.0/16',
            'nw-proto': 'ICMP',
            'action': 'DENY'
        }

        print(sdnc.addAclRule(rule1))
        print(sdnc.addAclRule(rule2))
        print(sdnc.addAclRule(rule3))
        print(sdnc.listAclRules())

        print('TASK 2 - TCP')
        # TASK 2 - TCP
        rule4 = {
            'src-ip': '172.16.0.101/32',
            'dst-ip': '192.168.0.101/32',
            'nw-proto': 'TCP',
            'action': 'ALLOW'
        }
        rule5 = {
            'src-ip': '10.0.0.101/32',
            'dst-ip': '192.168.0.101/32',
            'nw-proto': 'TCP',
            'action': 'ALLOW'
        }
        rule6 = {
            'src-ip': '172.16.0.0/16',
            'dst-ip': '192.168.0.101/32',
            'nw-proto': 'TCP',
            'action': 'DENY'
        }

        # print(sdnc.addAclRule(rule4))
        # print(sdnc.addAclRule(rule5))
        # print(sdnc.addAclRule(rule6))
        # print(sdnc.listAclRules())

        print('TASK 3 - UDP')
        # TASK 3 - UDP
        rule7 = {
            'src-ip': '192.168.0.102/32',
            'dst-ip': '10.0.0.102/32',
            'nw-proto': 'UDP',
            'action': 'ALLOW'
        }
        rule8 = {
            'src-ip': '172.16.0.102/32',
            'dst-ip': '10.0.0.102/32',
            'nw-proto': 'UDP',
            'action': 'ALLOW'
        }
        rule9 = {
            'src-ip': '172.16.0.0/16',
            'dst-ip': '10.0.0.102/32',
            'nw-proto': 'UDP',
            'action': 'DENY'
        }
        rule10 = {
            'src-ip': '192.168.0.0/24',
            'dst-ip': '10.0.0.102/32',
            'nw-proto': 'UDP',
            'action': 'DENY'
        }
        rule11 = {
            'src-ip': '10.0.0.0/8',
            'dst-ip': '10.0.0.102/32',
            'nw-proto': 'UDP',
            'action': 'DENY'
        }

        # print(sdnc.addAclRule(rule7))
        # print(sdnc.addAclRule(rule8))
        # print(sdnc.addAclRule(rule9))
        # print(sdnc.addAclRule(rule10))
        # print(sdnc.addAclRule(rule11))
        # print(sdnc.listAclRules())


    except Exception as e:
        print("Something went wrong " + str(e))
