from abc import ABC

from core.base_interfaces import GetInstanceInterface, GetAllInstancesInterface, CreateInstanceInterface, \
    UpdateInstanceInterface, DeleteInstanceInterface


class ArchitectorRepositoryInterface(
                           GetInstanceInterface,
                           GetAllInstancesInterface,
                           CreateInstanceInterface,
                           UpdateInstanceInterface,
                           DeleteInstanceInterface):
    pass


class ArchitectorServiceInterface(
                           GetInstanceInterface,
                           GetAllInstancesInterface,
                           CreateInstanceInterface,
                           UpdateInstanceInterface,
                           DeleteInstanceInterface):
    pass
