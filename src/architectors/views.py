from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from architectors.serializers import ArchitectorDTOSerializer
from architectors.services import ArchitectorServices


class ArchitectorAPI(APIView):
    def get(self, request, architector_id: int):
        """Get post detail by id"""
        post_interactor = ArchitectorServices()

        architector_dto = post_interactor.get_instance(architector_id)

        post_serializer = ArchitectorDTOSerializer(architector_dto)
        post_serializer_data = post_serializer.data
        return Response(
            {"post": post_serializer_data},
            status=status.HTTP_200_OK)
