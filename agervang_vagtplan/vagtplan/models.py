from django.db import models

# Create your models here.




class vagt(models.Model):
    dato = models.DateField()
    status = models.CharField(max_length=64)
    person = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.dato}: {self.status}, {self.person}"



