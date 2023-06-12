from itertools import repeat
from typing import List

from architectors.dto import ArchitectorDTO
from architectors.interfaces import ArchitectorRepositoryInterface
from architectors.models import Architector
from core.converters import ToDTOConverter


class ArchitectorRepository(ArchitectorRepositoryInterface):

    def __init__(self, converter: ToDTOConverter):
        self.converter = converter

    def get_instance(self, instance_id) -> ArchitectorDTO:
        architector = Architector.objects.prefetch_related("company").get(id=instance_id)
        return self.converter.to_dto_entity(architector, ArchitectorDTO)

    def get_all_instances(self) -> List[ArchitectorDTO]:
        architectors = Architector.objects.prefetch_related("company")
        return list(map(self.converter.to_dto_entity, architectors, repeat(ArchitectorDTO)))

    def create_instance(self):
        pass

    def update_instance(self):
        pass

    def delete_instance(self):
        pass
