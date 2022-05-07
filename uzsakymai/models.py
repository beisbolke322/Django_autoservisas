from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UzsakymuListas(models.Model):
    title = models.CharField("Pavadinimas", max_length=100, help_text="Pavadink šitą darbų seką kaip nors originaliai")

    class Meta:
        verbose_name = 'Uzsakymu listas'
        verbose_name_plural = 'Uzsakymu listai'

    def __str__(self):
        return self.title
        
class Uzsakymai(models.Model):
    dalis = models.CharField("dalis", max_length=30, help_text="Reikalinga dalis")
    uzsakyta = models.BooleanField(default=False)
    is_kur = models.CharField("vieta", max_length=30, help_text="Iš kur užsakyti", default="SA")
    kiekis = models.SmallIntegerField("kiekis", help_text="Koks dalių kiekis reikalingas", default=0)
    data = models.DateField(auto_now=True)
    list = models.ForeignKey(UzsakymuListas, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Dalis'
        verbose_name_plural = 'Dalys'

    def __str__(self):
        return self.dalis
        return self.is_kur
        return self.kiekis
       