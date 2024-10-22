from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework import exceptions

from app.models import Application
from app.serializer import CreateApplicationSerializer, DetailApplicationSerializer
from app.exceptions import error_exception, ErrorCodes


class CreateApplicationView(APIView):
    @extend_schema(
        summary="Application create",
        request=CreateApplicationSerializer,
        responses=status.HTTP_200_OK
    )
    def post(self, request):
        serializer = CreateApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        surname = serializer.validated_data['surname']
        phone = serializer.validated_data['phone']
        category = serializer.validated_data['category']

        Application.objects.create(
            name=name,
            surname=surname,
            phone=phone,
            category=category
        )
        return Response(status=status.HTTP_200_OK)


class DetailApplicationView(APIView):
    @extend_schema(
        summary="Application detail",
        request=DetailApplicationSerializer,
        responses=status.HTTP_200_OK
    )
    def get(self, request):
        serializer = DetailApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        Application.objects.filter(
            phone=phone
        ).first()
        try:
            Application.objects.get(
                phone=phone
            )
        except Application.DoesNotExist:
            raise error_exception(
                exceptions.NotFound,
                ErrorCodes.OBJECT_NOT_FOUND
            )
