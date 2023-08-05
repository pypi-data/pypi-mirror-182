import os
from abc import ABC


class Configuration(ABC):
    __root_folder = 'ksg_scheduling'

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        return None

    def project_path_to_relative(self, path: str):
        return path
        """
        Converts a path relative to the project root to a path relative to the execution root
        :param path: Project root relative path
        :return: Execution root relative path
        """
        sep = os.sep if path.count(os.sep) >= path.count(os.altsep) else os.altsep
        execution_nest = os.getcwd().split(self.__root_folder)[1].count(os.sep)
        return f'..{sep}' * execution_nest + path.lstrip(sep)

    def dump_config_params(self) -> tuple:
        ...
