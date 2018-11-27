from django.db import models

class Perro(models.Model):
    nombre = models.TextField(max_length=100)
    raza = models.TextField(max_length=100)
    descripciom = models.TextField(max_length=100)