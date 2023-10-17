from django.db import models

class Pertsona(models.Model):
    izena = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    nan = models.CharField(max_length=9)
    def __unicode__(self):
        return self.izena
    
class Etxea(models.Model):
    izena = models.CharField(max_length=100)
    herria = models.CharField(max_length=100)
    pertsonaKop = models.IntegerField()
    pertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.izena 
