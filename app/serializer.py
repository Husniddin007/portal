from rest_framework import serializers

from app.models import Application


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'name',
            'surname',
            'series',
            'jshshir',
            'phone',
            'category',
        ]



class DetailApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application


