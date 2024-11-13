from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework import status

from app.models import Application
from app.serializer import CreateApplicationSerializer, DetailApplicationSerializer



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
        series = serializer.validated_data['series']
        jshshir = serializer.validated_data['jshshir']
        Application.objects.get_or_create(
            name=name,
            surname=surname,
            series=series,
            jshshir=jshshir,
            phone=phone,
            category=category,
        )
        return Response(status=status.HTTP_200_OK)


class DetailApplicationView(APIView):
    @extend_schema(
        summary="Application detail",
        request=DetailApplicationSerializer,
        responses=status.HTTP_200_OK
    )
    def post(self, request):
        phone = request.query_params.get('phone')
        application = get_object_or_404(Application, phone=phone)
        serializer = DetailApplicationSerializer(application)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
