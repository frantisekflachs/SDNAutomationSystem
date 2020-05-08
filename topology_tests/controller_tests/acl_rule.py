from topology_tests.controller_tests.sdn_controller_test import SDNControllerTest
from sdn_controllers.floodlight import Floodlight


class AclRule(SDNControllerTest):
    """Testing for ACL rule in active rules aplied on SDN Controller"""

    def execute(self, params, SDNController):
        """ Execute the test for founding ACL rule in current rules applied on SDN Controller
        params: key value key value ... in template -> JSON to compare"""

        loadedParams = {}
        for p in range(0, len(params)):
            if not p % 2:
                loadedParams[params[p]] = params[p+1]

        # print(loadedParams)

        sdnc = Floodlight()
        # get ACL rules from SDN controller
        currentAclRules = sdnc.listAclRules()
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
