from django.db import models


class AdminLoginmodel(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)