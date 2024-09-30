from django.db import models

class Teachers(models.Model):
    nip = models.CharField(max_length=20, unique=True)  # NIP biasanya berupa string
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name

