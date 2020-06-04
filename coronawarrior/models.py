from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50,default='Nothing')
    desc = models.CharField(max_length=300,default='NOTHING')
    pub_date = models.DateField(default='2019-10-15')
    image = models.ImageField(upload_to='coronakit/images', default="")
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50,default='Nothing')
    category_desc=models.CharField(max_length=300,default="Nothing")

    def __str__(self):
        return self.category_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.email



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
