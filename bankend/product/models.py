from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50,default='books')
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=23.54)

    def __str__(self):
        return self.title


    # @property
    # def discount(self):
    #     discount = float(self.price) * 0.8
    #     return '%.2f' % discount