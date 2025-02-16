from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    history = models.TextField()
    sensei = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dojo_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    foto = models.ImageField(upload_to='eventos/', null=True, blank=True)

    def __str__(self):
        return self.titulo