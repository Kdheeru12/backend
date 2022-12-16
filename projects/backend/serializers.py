from user.models import User
from rest_framework import serializers


# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     username = serializers.CharField()
#     email = serializers.CharField()
#     # address = serializers.DictField(child=serializers.CharField())
#     website = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "name", "email", "website")
