from dataclasses import dataclass

from sampo.metrics.resources_in_time.service import ResourceOptimizationType
from sampo.scheduler.base import SchedulerType
from sampo.schemas.contractor import Contractor
from sampo.schemas.graph import WorkGraph
from sampo.schemas.serializable import AutoJSONSerializable
from sampo.schemas.time import Time
from sampo.schemas.time_estimator import WorkTimeEstimator
from sampo.utilities.serializers import custom_serializer
from sampo.utilities.task_name import NameMapper
from sampo.utilities.visualization.base import VisualizationMode
from sampo.utilities.visualization.resources import EmploymentFigType

from external.estimate_time import WorkTimeEstimationMode
from launch.schemas.configuration.base import Configuration


@dataclass
class SchedulingConfiguration(Configuration):
    input_configuration: 'SchedulingInputConfiguration'
    inner_configuration: 'SchedulingInnerConfiguration'
    output_configuration: 'SchedulingOutputConfiguration'

    def __getattr__(self, item):
        for member in self.input_configuration, self.output_configuration, self.inner_configuration:
            it = member.__getattr__(item)
            if it is not None:
                break
        return it

    def dump_config_params(self) -> tuple:
        return self.input_configuration.dump_config_params() \
            + self.inner_configuration.dump_config_params() \
            + self.output_configuration.dump_config_params()


@dataclass
class SchedulingInputConfiguration(AutoJSONSerializable['SchedulingInputConfiguration'], Configuration):
    work_graph: WorkGraph
    contractors: list[Contractor]

    @custom_serializer('contractors')
    def contractors_serializer(self, value):
        return [c._serialize() for c in value]

    @classmethod
    @custom_serializer('contractors', deserializer=True)
    def contractors_deserializer(cls, value):
        return [Contractor._deserialize(c) for c in value]

    def dump_config_params(self) -> tuple:
        return self.work_graph, self.contractors


class SchedulingInnerConfiguration(Configuration):
    start: str
    end: str
    algorithm_type: SchedulerType
    resource_optimization: ResourceOptimizationType | None
    use_idle_estimator: bool
    validate_schedule: bool
    deadline: Time | None
    estimator_mode: WorkTimeEstimationMode | None
    inverse_name_mapper: NameMapper | None
    work_time_estimator: WorkTimeEstimator | None

    def __init__(self, algorithm_type: SchedulerType, start: str, end: str, validate_schedule: bool):
        self.algorithm_type = algorithm_type
        self.start = start
        self.end = end
        self.validate_schedule = validate_schedule

        self.deadline = None
        self.estimator_mode = None
        self.resource_optimization = None
        self.inverse_name_mapper = None
        self.work_time_estimator = None

    def with_work_time_estimator(self, work_time_estimator: WorkTimeEstimator,
                                 use_idle_estimator: bool,
                                 estimator_mode: WorkTimeEstimationMode | None = WorkTimeEstimationMode.Realistic) \
            -> 'SchedulingInnerConfiguration':
        self.work_time_estimator = work_time_estimator
        self.use_idle_estimator = use_idle_estimator
        self.estimator_mode = estimator_mode
        return self

    def with_deadline_resource_optimization(self, deadline: Time, optimization_type: ResourceOptimizationType) \
            -> 'SchedulingInnerConfiguration':
        self.deadline = deadline
        self.resource_optimization = optimization_type
        return self

    def with_inverse_name_mapper(self, inverse_name_mapper: NameMapper) -> 'SchedulingInnerConfiguration':
        self.inverse_name_mapper = inverse_name_mapper
        return self

    def dump_config_params(self) -> tuple:
        return (self.start,
                self.end,
                self.deadline,
                self.algorithm_type,
                self.resource_optimization,
                self.work_time_estimator,
                self.use_idle_estimator,
                self.estimator_mode,
                self.inverse_name_mapper,
                self.validate_schedule)


class SchedulingOutputConfiguration(Configuration):
    title: str
    output_folder_path: str
    save_to_xer: bool
    save_to_csv: bool
    save_to_json: bool
    gant_chart_visualization: VisualizationMode
    employment_figs: list[EmploymentFigType | VisualizationMode] | None

    def __init__(self, title: str, output_folder: str, save_to_xer: bool, save_to_csv: bool, save_to_json: bool):
        self.title = title
        self.output_folder_path = output_folder
        self.save_to_xer = save_to_xer
        self.save_to_csv = save_to_csv
        self.save_to_json = save_to_json

        self.employment_figs = None

    def with_gant_chart(self, visualization_mode: VisualizationMode) -> 'SchedulingOutputConfiguration':
        self.gant_chart_visualization = visualization_mode
        return self

    def with_one_more_employment_fig(self, fig_type: EmploymentFigType, visualization_mode: VisualizationMode) \
            -> 'SchedulingOutputConfiguration':
        if self.employment_figs is None:
            self.employment_figs = list()
        self.employment_figs.append((fig_type, visualization_mode))
        return self

    def dump_config_params(self) -> tuple:
        return (self.title,
                self.project_path_to_relative(self.output_folder_path),
                self.save_to_xer,
                self.save_to_csv,
                self.save_to_json,
                self.gant_chart_visualization,
                self.employment_figs)
