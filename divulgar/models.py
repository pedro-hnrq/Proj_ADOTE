from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Pet(models.Model):
    choises_status = (('P', 'Para adocao'),
                      ('A', 'Adotado'))
    # on_delete=models.Cascate = usuario poderá cadastra vários Pet, só que quando excluido o usuário será elimando os Pet desse mesmo que foi cadastrado.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)    
    telefone = models.CharField(max_length=16)
    # ManyToManyField = relação de Muito x Muito 
    tags = models.ManyToManyField(Tag)
    # on_delete=models.DO_NOTHIN = acontece nada!
    raca  = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choises_status, default='P')

    def __str__(self):
        return self.nome