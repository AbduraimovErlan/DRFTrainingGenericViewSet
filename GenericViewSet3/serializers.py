from rest_framework import serializers
from GenericViewSet3.models import Book3



class SerializersBook3(serializers.ModelSerializer):
    class Meta:
        model = Book3
        fields = '__all__'