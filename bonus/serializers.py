from rest_framework import serializers

from bonus.models import BonusCategory, UserBlock


class BonusCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusCategory
        fields = [
            'id',
            'name',
            'merchant',
            'icon',
            'created_at',
        ]
        extra_kwargs = {
            'merchant': {'read_only': True},
            'created_at': {'read_only': True},
        }
    
    def validate(self, attrs):
        attrs['merchant'] = self.context['request'].user.merchant
        return attrs


class UserBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlock
        fields = [
            'id',
            'username',
            'merchant',
            'is_active',
            'created_at',
        ]
        extra_kwargs = {
            'merchant': {'read_only': True},
            'created_at': {'read_only': True},
        }
    
    def validate(self, attrs):
        attrs['merchant'] = self.context['request'].user.merchant
        return attrs
