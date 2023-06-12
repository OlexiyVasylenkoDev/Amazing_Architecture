from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from architectors.serializers import ArchitectorDTOSerializer
from core.containers import ServiceContainer


class ArchitectorAPI(APIView):

    def get(self, request):
        architector_service = ServiceContainer.architector_service()

        architector_dto = architector_service.get_all_instances()

        architectors_serializer = ArchitectorDTOSerializer(architector_dto, many=True)
        architectors_serializer_data = architectors_serializer.data
        return Response(
            {"post": architectors_serializer_data},
            status=status.HTTP_200_OK)


class ArchitectorDetailAPI(APIView):
    def get(self, request, architector_id: int):
        """Get post detail by id"""
        architector_service = ServiceContainer.architector_service()

        architector_dto = architector_service.get_instance(architector_id)

        architector_serializer = ArchitectorDTOSerializer(architector_dto)
        architector_serializer_data = architector_serializer.data

        return Response(
            {"post": architector_serializer_data},
            status=status.HTTP_200_OK)
