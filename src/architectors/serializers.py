from rest_framework import serializers


class CompanyDTOSerializer(serializers.Serializer):
    title = serializers.CharField()
    number_of_employees = serializers.IntegerField()


class ArchitectorDTOSerializer(serializers.Serializer):
    company = CompanyDTOSerializer(many=True, read_only=True)

    name = serializers.CharField()
    age = serializers.IntegerField()
    is_active = serializers.BooleanField()
