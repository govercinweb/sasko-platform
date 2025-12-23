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
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    # def validate(self, data):
    #     raise serializers.ValidationError('this is error!')
    #     # import time
    #     # time.sleep(10)
    #     # return data
