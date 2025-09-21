from django.db import models

DIFFICULTY_CHOICES = [
    ('F', 'Fácil'),
    ('M', 'Médio'),
    ('D', 'Difícil'),
]

class Drink(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    dificuldade = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='F')
    ingredientes = models.CharField(max_length=500, blank=True) 
    imagem = models.ImageField(upload_to='drinks/', null=True, blank=True)  

    def __str__(self):
        return self.nome