from django.contrib.auth.hashers import check_password, make_password
from django.utils.translation import gettext as _
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


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = [
            'id',
            'old_password',
            'new_password',
            'confirm_password',
        ]

    def validate(self, attrs):
        old_pass = attrs['old_password']
        if not check_password(old_pass, self.instance.password):
            raise serializers.ValidationError(_('Existing password is incorrect.'))

        new_pass = attrs['new_password']
        confirm_pass = attrs['confirm_password']
        if not new_pass or new_pass != confirm_pass:
            raise serializers.ValidationError(_('New passwords does bot match.'))
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['new_password'])
        instance.save()
        return instance
