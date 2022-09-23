from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Videos(models.Model):
    nome_videos = models.CharField(max_length=50)
    link_videos = models.CharField(max_length=100)
    desc_videos = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Video'

    def __str__(self):
        return self.nome_videos

class Games(models.Model):
    nome_games = models.CharField(max_length=50)
    link_games = models.CharField(max_length=100)
    desc_games = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Game'

    def __str__(self):
        return self.nome_games

class Atividades(models.Model):
    nome_atividades = models.CharField(max_length=50)
    link_atividades = models.CharField(max_length=100)
    desc_atividades = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Atividades'

    def __str__(self):
        return self.nome_atividades