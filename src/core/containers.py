from dependency_injector import containers, providers

from architectors.repository import ArchitectorRepository
from architectors.services import ArchitectorServices
from core.converters import FromOrmToDTO


class ConvertorsContainer(containers.DeclarativeContainer):
    from_queryset_to_dto = providers.Factory(FromOrmToDTO)


class RepositoryContainer(containers.DeclarativeContainer):
    architector_repository = providers.Factory(
        ArchitectorRepository,
        converter=ConvertorsContainer.from_queryset_to_dto
    )


class ServiceContainer(containers.DeclarativeContainer):
    architector_service = providers.Factory(
        ArchitectorServices,
        repository=RepositoryContainer.architector_repository
    )
