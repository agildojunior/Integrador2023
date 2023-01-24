from django.db import models


class Adress(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerai"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RR", "Roraima"),
        ("RO", "Rondônia"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    street = models.CharField(verbose_name="Rua", max_length=255)
    number = models.CharField(verbose_name="Número", max_length=20)
    district = models.CharField(verbose_name="Bairro", max_length=50)
    cep = models.CharField(verbose_name="CEP", max_length=12)
    city = models.CharField(verbose_name="Cidade", max_length=50)
    state = models.CharField(
        verbose_name="Estado",
        max_length=30,
        choices=ESTADO_CHOICES,
        blank=False,
        null=False,
    )
    complement = models.CharField(verbose_name="Complemento", max_length=255)
    user = models.ForeignKey("User", verbose_name="Usuário", on_delete=models.CASCADE)

    def __str__(self):
        return self.city
