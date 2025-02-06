from django.db import models

# Create your models here.
class ProfissionalSaude(models.Model):
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    profissao = models.CharField(max_length=255)
    endereco = models.TextField()
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo


class Consulta(models.Model):
    data_consulta = models.DateTimeField()
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name="consultas")

    def __str__(self):
        return f"{self.data_consulta} - {self.profissional.nome_completo}"
