from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    # to change list view in django admin
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'List of Subscribers'
