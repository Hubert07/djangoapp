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
    opis = models.TextField(blank=True, default='', help_text='opis pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=MEDIUM)
    cena =  models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data = models.DateField('dodano', auto_now_add=True)


class Skladniki(models.Model):
    pizza = models.ManyToManyField(Pizza, related_name='skladniki')
    nazwa = models.CharField(verbose_name='skladnik', max_length=30)
    jarski = models.BooleanField(verbose_name='jarski?',
                                 help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian',
                                 default=False)