from post_configurations.topology1PostConfig import Topology1PostConfig
from post_configurations.topology2PostConfig import Topology2PostConfig
from post_configurations.topology3PostConfig import Topology3PostConfig
from post_configurations.topology4PostConfig import Topology4PostConfig
from post_configurations.topology5PostConfig import Topology5PostConfig
from post_configurations.topology6PostConfig import Topology6PostConfig


class PostConfigExecutor:
    """Executor for post configurations defined in topology template yaml file"""

    def __init__(self, SDNController):
        self.sdnc = SDNController
        self.implementedPostConfigs = {
            'topology1PostConfig': Topology1PostConfig(),
            'topology2PostConfig': Topology2PostConfig(),
            'topology3PostConfig': Topology3PostConfig(),
            'topology4PostConfig': Topology4PostConfig(),
            'topology5PostConfig': Topology5PostConfig(),
            'topology6PostConfig': Topology6PostConfig(),
        }

    def run(self, postConfigFromTemplate):
        """Run choosen topology post configuration"""

        try:
            conf = self.implementedPostConfigs[postConfigFromTemplate]
            ret = conf.execute(self.sdnc)
            return ret

        except Exception as e:
            print("Something went wrong " + str(e))
