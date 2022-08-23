from django.db import models

# Create your models here.
class test(models.model):
    col1 = models.CharField(max_length=30)
    class Meta:
        db_table = "test_table"