from django.db import models

# Create your models here.
class signup(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)
    role = models.IntegerField(default=0)
    class Meta:
        db_table=('Register')

class Contact(models.Model):
    con_id =models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    class Meta:
        db_table=('Contact')

class addItems(models.Model):
    iid =models.AutoField(primary_key=True)
    item_image = models.ImageField(upload_to='media/')
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50)    
    dis = models.CharField(max_length=500)
    class Meta:
        db_table=('additems')

class Cart(models.Model):
    cid = models.AutoField(primary_key=True)
    iid = models.IntegerField()
    user = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    class Meta:
        db_table=('Ecommerce_app_cart')


class Payment(models.Model):
    pid = models.AutoField(primary_key=True)
    iid = models.IntegerField()
    user = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    pay_mode = models.CharField(max_length=100)
    total = models.IntegerField()
    class Meta:
        db_table=('Payment')

class OnlinePayment(models.Model):
    opid = models.AutoField(primary_key=True)
    iid = models.IntegerField()
    user = models.CharField(max_length=50)
    phone = models.IntegerField()
    tid = models.IntegerField()
    gtotal = models.IntegerField()
    class Meta:
        db_table=('Online_Payment')
    