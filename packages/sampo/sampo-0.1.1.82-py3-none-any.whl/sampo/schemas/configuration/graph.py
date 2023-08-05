from enum import auto, Enum
from random import Random
from typing import Union

from pandas import DataFrame
from sampo.generator.pipeline.project import SyntheticGraphType
from sampo.schemas.contractor import ContractorName
from sampo.schemas.types import WorkerName
from sampo.utilities.task_name import NameMapper
from sampo.utilities.visualization.base import VisualizationMode

from external.contractor_type import ContractorType
from external.estimate_time import WorkResourceEstimator
from external.lib.contractor_team import ContractorTeam
from launch.schemas.configuration.base import Configuration


class GraphConfigurationType(Enum):
    Generate = auto()
    ReadGraphGenerateResources = auto()
    ReadGraph = auto()


class GraphConfiguration(Configuration):
    type: GraphConfigurationType
    graph_info_file: Union[str, DataFrame] | None
    use_graph_lag_optimization: bool | None
    graph_fig_visualization: VisualizationMode | None
    generate_input: bool | None
    graph_mode: SyntheticGraphType | None
    synthetic_graph_vertices_lower_bound: int | None
    contractor_type: ContractorName | None
    contractor_team: WorkerName | None
    use_task_resource_generation: bool | None
    unique_work_names_mapper: NameMapper | None
    work_resource_estimator: WorkResourceEstimator | None

    def __init__(self,
                 graph_info_file: Union[str, DataFrame] | None = None,
                 use_graph_lag_optimization: bool | None = None,
                 graph_fig_visualization: VisualizationMode | None = VisualizationMode.NoFig,
                 generate_input: bool | None = None,
                 rand: Random | None = None,
                 graph_mode: SyntheticGraphType | None = None,
                 synthetic_graph_vertices_lower_bound: int | None = None,
                 contractor_type: ContractorName | None = None,
                 contractor_team: WorkerName | None = None,
                 use_task_resource_generation: bool | None = None,
                 unique_work_names_mapper: NameMapper | None = None,
                 work_resource_estimator: WorkResourceEstimator | None = None):
        self.graph_info_file = graph_info_file
        self.use_graph_lag_optimization = use_graph_lag_optimization
        self.graph_fig_visualization = graph_fig_visualization
        self.generate_input = generate_input
        self.rand = rand
        self.graph_mode = graph_mode
        self.synthetic_graph_vertices_lower_bound = synthetic_graph_vertices_lower_bound
        self.contractor_type = contractor_type
        self.contractor_team = contractor_team
        self.use_task_resource_generation = use_task_resource_generation
        self.unique_work_names_mapper = unique_work_names_mapper
        self.work_resource_estimator = work_resource_estimator

    def with_visualization(self, visualization_mode: VisualizationMode) -> 'GraphConfiguration':
        self.graph_fig_visualization = visualization_mode
        return self

    @staticmethod
    def generate_graph(graph_mode: SyntheticGraphType,
                       use_graph_lag_optimization: bool,
                       contractor_capacity: list[int] = [ContractorType.Average.command_capacity()],
                       contractor_team: list[str] = [ContractorTeam.Multi.resources_list()],
                       synthetic_graph_vertices_lower_bound: int | None = 200,
                       rand: Random | None = None) -> 'GraphConfiguration':
        config = GraphConfiguration(generate_input=True,
                                    graph_mode=graph_mode,
                                    use_graph_lag_optimization=use_graph_lag_optimization,
                                    contractor_type=contractor_capacity,
                                    contractor_team=contractor_team,
                                    synthetic_graph_vertices_lower_bound=synthetic_graph_vertices_lower_bound,
                                    rand=rand)
        config.type = GraphConfigurationType.Generate
        return config

    @staticmethod
    def read_graph_generate_resources(graph_info: Union[str, DataFrame],
                                      use_graph_lag_optimization: bool,
                                      work_resource_estimator: WorkResourceEstimator,
                                      contractor_capacity: list[int] = [ContractorType.Average.command_capacity()],
                                      contractor_resources: list[str] = [ContractorTeam.Multi.resources_list()],
                                      unique_work_names_mapper: NameMapper | None = None) -> 'GraphConfiguration':
        config = GraphConfiguration(use_task_resource_generation=True,
                                    graph_info_file=graph_info,
                                    use_graph_lag_optimization=use_graph_lag_optimization,
                                    contractor_type=contractor_capacity,
                                    contractor_team=contractor_resources,
                                    work_resource_estimator=work_resource_estimator,
                                    unique_work_names_mapper=unique_work_names_mapper)
        config.type = GraphConfigurationType.ReadGraphGenerateResources
        return config

    @staticmethod
    def read_graph(graph_info_filepath: str,
                   use_graph_lag_optimization: bool,
                   work_resource_estimator: WorkResourceEstimator | None = None) -> 'GraphConfiguration':
        config = GraphConfiguration(graph_info_file=graph_info_filepath,
                                    use_graph_lag_optimization=use_graph_lag_optimization,
                                    work_resource_estimator=work_resource_estimator)
        config.type = GraphConfigurationType.ReadGraph
        return config

    def dump_config_params(self) -> tuple:
        return (self.project_path_to_relative(self.graph_info_file)
                    if isinstance(self.graph_info_file, str)
                    else self.graph_info_file,
                self.use_graph_lag_optimization,
                self.graph_fig_visualization,
                self.generate_input,
                self.rand,
                self.graph_mode,
                self.synthetic_graph_vertices_lower_bound,
                self.contractor_type,
                self.contractor_team,
                self.use_task_resource_generation,
                self.unique_work_names_mapper,
                self.work_resource_estimator)
