from topology_tests.controller_tests.sdn_controller_test import SDNControllerTest
from sdn_controllers.floodlight import Floodlight


class FlowRule(SDNControllerTest):
    """Testing for Flow rule in active flows aplied on SDN Controller"""

    def execute(self, params, SDNController):
        """ Execute the test for founding Flow rule in current flows applied on SDN Controller
        params: key value key value ... in template -> JSON to compare"""

        loadedParams = {}
        for p in range(0, len(params)):
            # print(params[p])
            if not p % 2:
                loadedParams[params[p]] = params[p+1]
        # print('Loaded params:', loadedParams)

        # get Flow rules from SDN controller
        allCurrentFlowRules = SDNController.listFlowTable(loadedParams['switch_id'])
        currentFlowRules = allCurrentFlowRules[loadedParams['switch_id']]
        # print(currentFlowRules)

        loadedParams.pop('switch_id')
        # print('Loaded params:', loadedParams)

        # compare rules from SDNC and loaded from template
        found = False
        for currentFlowRule in currentFlowRules:
            # print(currentFlowRule)
            if loadedParams['name'] in currentFlowRule.keys():
                # print(currentFlowRule.keys())
                foundRule = currentFlowRule[loadedParams['name']]
                for key, values in loadedParams.items():
                    if key in foundRule.keys():
                        # print(key)
                        if str(loadedParams[key]) == str(foundRule[key]):
                            # print(loadedParams[key])
                            found = True
                        else:
                            found = False
                            continue
                    else:
                        continue
                # rule by definition from template is founded in flows from SDNC
                if found:
                    # print('flows founded')
                    return True
        # flows was not founded
        if not found:
            return False
