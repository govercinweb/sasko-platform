from django.db import models


class BonusCategory(models.Model):
    merchant = models.ForeignKey('accounts.Merchant', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
