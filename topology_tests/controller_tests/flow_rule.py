from topology_tests.topology_test import TopologyTest
from sdn_controllers.floodlight import Floodlight


class FlowRule(TopologyTest):
    """Testing for Flow rule in active flows aplied on SDN Controller"""

    def execute(self, params):
        """ Execute the test for founding Flow rule in current flows applied on SDN Controller
        params: key value key value ... in template -> JSON to compare"""

        loadedParams = {}
        for p in range(0, len(params)):
            if not p % 2:
                loadedParams[params[p]] = params[p+1]

        # print(loadedParams)

        sdnc = Floodlight()
        # get Flow rules from SDN controller
        currentFlowRules = sdnc.listFlowTable('all')
        print(currentFlowRules)

        # compare rules from SDNC and loaded from template
        found = False
        for currentFlowRule in currentFlowRules:
            # print(currentFlowRule)
            for key, values in loadedParams.items():
                if key in currentFlowRule.keys():
                    # print(key)
                    if str(loadedParams[key]) == str(currentFlowRule[key]):
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
