from launch.schemas.configuration.base import Configuration
from launch.schemas.configuration.graph import GraphConfiguration
from launch.schemas.configuration.scheduling import SchedulingConfiguration


class LaunchConfiguration(Configuration):
    graph_config: GraphConfiguration
    scheduling_config: SchedulingConfiguration

    def __init__(self, graph_config: GraphConfiguration, scheduling_config: SchedulingConfiguration):
        self.graph_config = graph_config
        self.scheduling_config = scheduling_config

    def dump_config_params(self):
        return self.graph_config.dump_config_params(), self.scheduling_config.dump_config_params()
