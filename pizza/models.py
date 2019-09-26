from django.db import models

class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'Duża, 45cm'),
        (MEDIUM, 'Średnia, 38cm'),
        (SMALL, 'Mała, 25cm'),
    )

    nazwa = models.CharField(verbose_name='Pizza', max_length=30)
    opis = models.TextField(blank=True, help_text='opis pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=MEDIUM)
    cena =  models.DecimalField(max_digits=5, decimal_places=2)


class Skladniki(models.Model):
    pizza = models.ForeignKey()