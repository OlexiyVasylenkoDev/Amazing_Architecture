from architectors.repository import ArchitectorRepository
from core.base_interfaces import InstanceServiceInterface


class ArchitectorServices(InstanceServiceInterface):
    def get_instance(self, instance_id):
        repo = ArchitectorRepository()
        instance = repo.get_instance(instance_id=instance_id)
        return instance

    def get_all_instances(self):
        pass

    def create_instance(self):
        pass

    def update_instance(self):
        pass

    def delete_instance(self):
        pass

