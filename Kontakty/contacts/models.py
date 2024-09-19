from django.db import models


class kontakt(models.Model):
    meno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cislo = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title