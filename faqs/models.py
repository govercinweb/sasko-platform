from django.db import models

from auditlog.registry import auditlog


class FaqTag(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


auditlog.register(
    FaqTag,
    exclude_fields=['created_at', 'updated_at'],
)


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=800)
    order = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    tag = models.ForeignKey(FaqTag, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


auditlog.register(
    Faq,
    exclude_fields=['created_at', 'updated_at'],
)
