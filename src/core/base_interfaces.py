from abc import ABC, abstractmethod


class GetInstanceInterface(ABC):
    @abstractmethod
    def get_instance(self, instance_id):
        pass


class GetAllInstancesInterface(ABC):
    @abstractmethod
    def get_all_instances(self):
        pass


class CreateInstanceInterface(ABC):
    @abstractmethod
    def create_instance(self):
        pass


class UpdateInstanceInterface(ABC):
    @abstractmethod
    def update_instance(self):
        pass


class DeleteInstanceInterface(ABC):
    @abstractmethod
    def delete_instance(self):
        pass


class InstanceDTOInterface(ABC):
    @abstractmethod
    def instance_dto(self, instance):
        pass

    @abstractmethod
    def all_instances_dto(self):
        pass
