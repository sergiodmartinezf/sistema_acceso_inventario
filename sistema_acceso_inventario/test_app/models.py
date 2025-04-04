from django.db import models

# Create your models here.
class tabla1(models.Model):
    id=models.AutoField(primary_key=True)
    dato1=models.IntegerField()
    dato2=models.CharField(max_length=100)
