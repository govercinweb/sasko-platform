from django.db import models


class BonusCategory(models.Model):
    merchant = models.ForeignKey('accounts.Merchant', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserBlock(models.Model):
    merchant = models.ForeignKey('accounts.Merchant', on_delete=models.CASCADE)
    username = models.CharField(max_length=250)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('merchant', 'username')

    def __str__(self):
        return f"{self.username}"
