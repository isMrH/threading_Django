from django.db import models

# Create your models here.
class SQLlist(models.Model):
    category = models.CharField(max_length=50)
    sql_text = models.CharField(max_length=100)



class datalist(models.Model):
    count = models.IntegerField()
    money = models.CharField(max_length=50)
    time = models.DateTimeField()
    category = models.CharField(max_length=50)






