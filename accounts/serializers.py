from rest_framework import serializers

from accounts.models import User


class ProfileDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
