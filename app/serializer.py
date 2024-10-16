from rest_framework import serializers

from app.models import Application


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'name',
            'surname',
            'phone',
            'category',
        ]
class DetailApplicationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)

