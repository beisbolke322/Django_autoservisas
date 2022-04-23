from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DarbuListas(models.Model):
    title = models.CharField("Pavadinimas", max_length=100, help_text="Pavadink šitą darbų seką kaip nors originaliai")
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Darbu listas'
        verbose_name_plural = 'Darbu listai'

    def __str__(self):
        return self.title
        # return self.user

class DarboDuomenys(models.Model):
    marke = models.CharField("A_marke", max_length=30, help_text="Automobilio markė")
    modelis = models.CharField("A_modelis", max_length=20, help_text="Automobilio modelis")
    sav = models.CharField("A_sav", max_length=70, help_text="Automobilio savininko vardas, pavardė")
    suged = models.CharField("A_sugedimai", max_length=200, help_text="Automobilio sugedimai/pakeitimai")
    isCompleted = models.BooleanField(default=False)
    list = models.ForeignKey(DarbuListas, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Darbo itemas'
        verbose_name_plural = 'Darbo itemai'

    def __str__(self):
        return self.marke
        return self.modelis
        return self.sav
        return self.suged
