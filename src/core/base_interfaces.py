from abc import ABC, abstractmethod


class InstanceServiceInterface(ABC):
    @abstractmethod
    def get_instance(self, instance_id):
        pass

    @abstractmethod
    def get_all_instances(self):
        pass

    @abstractmethod
    def create_instance(self):
        pass

    @abstractmethod
    def update_instance(self):
        pass

    @abstractmethod
    def delete_instance(self):
        pass
