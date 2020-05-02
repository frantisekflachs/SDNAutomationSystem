from topology_tests.topology_test import TopologyTest
from sdn_controllers.floodlight import Floodlight


class FwRule(TopologyTest):
    """Testing for firewall rule in active rules aplied on SDN Controller"""

    def execute(self, params):
        """ Execute the test for founding firewall rule in current rules applied on SDN Controller
        params: key value key value ... in template -> JSON to compare"""

        loadedParams = {}
        for p in range(0, len(params)):
            if not p % 2:
                loadedParams[params[p]] = params[p+1]

        # print(loadedParams)

        sdnc = Floodlight()
        # get FW rules from SDN controller
        currentAclRules = sdnc.firewallListRules()
        # print(currentAclRules)

        # compare rules from SDNC and loaded from template
        found = False
        for currentAclRule in currentAclRules:
            # print(currentAclRule)
            for key, values in loadedParams.items():
                if key in currentAclRule.keys():
                    # print(key)
                    if str(loadedParams[key]) == str(currentAclRule[key]):
                        # print(loadedParams[key])
                        found = True
                    else:
                        found = False
                        continue
                else:
                    continue
            # rule by definition from template is founded in rules from SDNC
            if found:
                # print('rule founded')
                return True
        # rule was not founded
        if not found:
            return False
