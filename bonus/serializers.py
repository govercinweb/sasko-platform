from rest_framework import serializers

from bonus.models import BonusCategory


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
