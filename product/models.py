from django.db import models

class Manufact(models.Model):
    name_man = models.TextField(max_length=50)


class Headphones(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    product_cost = models.IntegerField()
    realise_date = models.DateTimeField()
    fabric = models.ForeignKey(
        Manufact,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    img = models.ImageField(upload_to='images')





