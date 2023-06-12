from architectors.interfaces import ArchitectorRepositoryInterface
from core.base_interfaces import \
    GetInstanceInterface, \
    GetAllInstancesInterface, \
    CreateInstanceInterface, \
    UpdateInstanceInterface, \
    DeleteInstanceInterface


class ArchitectorServices(GetInstanceInterface,
                          GetAllInstancesInterface,
                          CreateInstanceInterface,
                          UpdateInstanceInterface,
                          DeleteInstanceInterface, ):

    def __init__(self, repository: ArchitectorRepositoryInterface):
        self.repository = repository

    def get_instance(self, instance_id: int):
        return self.repository.get_instance(instance_id=instance_id)

    def get_all_instances(self):
        return self.repository.get_all_instances()

    def create_instance(self):
        pass

    def update_instance(self):
        pass

    def delete_instance(self):
        pass
