from django.db import models

class Miasto(models.Model):
    miasto = models.CharField(max_length=25)
    kod = models.CharField(max_length=6)


class Uczelnia(models.Model):
    nazwa = models.CharField(max_length=50)


class Student(models.Model):
    imie = models.CharField(max_length=18)
    nazwissko = models.CharField(max_length=20)
    id_uczelni = models.ForeignKey(Uczelnia, related_name="studenci", on_delete=models.CASCADE)
    id_miasta = models.ForeignKey(Miasto, related_name="mieszkancy", on_delete=models.CASCADE)
    rok_studiow = models.CharField(max_length=10)
    dochod = models.DecimalField(decimal_places=2, max_digits=10)