from django.db import models


class FaqTag(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=800)
    order = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    tag = models.ForeignKey(FaqTag, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
