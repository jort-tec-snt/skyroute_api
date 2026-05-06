from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Flight(models.Model):
    code = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    airline = models.ForeignKey(
        Airline,
        on_delete=models.CASCADE,
        related_name='flights'
    )

    def __str__(self):
        return self.code