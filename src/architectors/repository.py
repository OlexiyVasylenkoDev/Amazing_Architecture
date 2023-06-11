from architectors.dto import ArchitectorDTO, CompanyDTO
from architectors.models import Architector
from core.base_interfaces import InstanceServiceInterface, InstanceDTOInterface
from core.converter import FromOrmToDTO


class ArchitectorRepository(InstanceServiceInterface, InstanceDTOInterface):
    def get_instance(self, instance_id):
        architector = Architector.objects.prefetch_related("company").get(id=instance_id)

        return architector

    def get_all_instances(self):
        pass

    def create_instance(self):
        pass

    def update_instance(self):
        pass

    def delete_instance(self):
        pass

    def instance_dto(self, instance):

        dto = FromOrmToDTO().to_dto_entity(self.get_instance(instance_id=instance.id), ArchitectorDTO)
        return dto

    def all_instances_dto(self):
        pass
