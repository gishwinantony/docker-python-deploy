from django.db import models

# Create your models here.

class Products(models.Model):
    product_name=models.CharField( max_length=50)
    product_qty=models.IntegerField()
    email=models.CharField(max_length=100)
    
    class Meta:
        db_table='product'
    
    def __str__(self):
        return f'{self.product_name} '       
    