from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

#Here the null parameter allows the data to be class to be accessed without fill all the variable while using template rendering
    def __str__(self):
        return self.name
# #This returns the object name so while you create a new customer object it will display it's name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door')
        )
    name = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True,blank=True)#Allows to be left blank aswell
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete= models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    def __str__(self):
        return self.product