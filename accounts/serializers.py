from django.contrib.auth.hashers import check_password, make_password
from django.utils.translation import gettext as _
from rest_framework import serializers

from accounts.models import User, InSiteNotificationUserInteraction, InSiteNotification, Merchant, \
    InfrastructureCredential
from commerce.serializers import CurrencySerializer


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

    def validate(self, data):
        if len(data['first_name']) <= 2:
            raise serializers.ValidationError({'first_name': _('First name can not be less then 3 characters.')})
        if len(data['last_name']) <= 2:
            raise serializers.ValidationError({'first_name': _('Last name can not be less then 3 characters.')})
        return data


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


class InSiteNotificationUserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InSiteNotificationUserInteraction
        fields = [
            'id',
            'is_deleted',
            'is_read',
            'user',
        ]
        extra_kwargs = {
            'user': {'read_only': True},
        }


class InSiteNotificationSerializer(serializers.ModelSerializer):
    interactions = InSiteNotificationUserInteractionSerializer(many=True)
    delivered_at = serializers.SerializerMethodField()

    class Meta:
        model = InSiteNotification
        fields = [
            'id',
            'subject',
            'body',
            'type',
            'user',
            'interactions',
            'delivered_at',
        ]
        extra_kwargs = {
            'subject': {'read_only': True},
            'body': {'read_only': True},
            'type': {'read_only': True},
            'user': {'read_only': True},
            'interactions': {'read_only': True},
        }

    @staticmethod
    def get_delivered_at(obj):
        if obj.start_showing_at:
            return obj.start_showing_at
        return obj.created_at


class InSiteNotificationChangeReadStatusSerializer(serializers.Serializer):
    in_site_notifications = serializers.PrimaryKeyRelatedField(queryset=InSiteNotification.objects.all(), many=True)
    mark_as = serializers.ChoiceField(choices=['read', 'unread', 'deleted'])

    def create(self, validated_data):
        return self.update(None, validated_data)

    def update(self, instance, validated_data):
        for notification in validated_data['in_site_notifications']:
            defaults = {}
            mark = validated_data['mark_as']
            if mark in ['read', 'unread']:
                defaults['is_read'] = mark == 'read'
            elif mark in ['deleted']:
                defaults['is_deleted'] = True
            InSiteNotificationUserInteraction.objects.update_or_create(
                notification=notification,
                user=self.context['request'].user,
                defaults=defaults,
            )
        return validated_data


class MerchantSerializer(serializers.ModelSerializer):
    # currency = CurrencySerializer()

    class Meta:
        model = Merchant
        fields = [
            'id',
            'name',
            'infrastructure',
            'currency',
            'main_domain',
            'is_transaction_fetching_active',
            'is_active',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['currency'] = CurrencySerializer(instance.currency).data
        return data


class InfrastructureCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureCredential
        fields = [
            'id',
            'email',
            'password',
            'otp_secret',
            'is_active',
            'created_at',
            'merchant',
        ]

        extra_kwargs = {
            'created_at': {'read_only': True},
            # 'merchant': {'write_only': True},
        }
