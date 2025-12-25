from rest_framework import serializers

from faqs.models import Faq, FaqTag


class FaqTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqTag
        fields = [
            'id',
            'name',
            'order',
        ]


class FaqSerializer(serializers.ModelSerializer):
    tag = FaqTagSerializer()

    class Meta:
        model = Faq
        fields = [
            'id',
            'question',
            'order',
            'answer',
            'tag',
        ]
