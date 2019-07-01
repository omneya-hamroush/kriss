from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class ProductManager(models.Manager):
    def create_product(self, name, description, price, product_image):
        if not name:
            raise ValueError('Product must have a name')


        product = self.model(name=name, description=description, price=price, product_image=product_image)


        product.save(using=self._db)

        return product



class Product (models.Model):
     name = models.CharField('Product name',max_length=255)
     description=models.TextField(max_length=2000)
     price=models.DecimalField(max_digits=10, decimal_places=2)
     is_available = models.BooleanField(default=True)
     product_image = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")

     REQUIRED_FIELDS= ['name']
     objects= ProductManager()
    #  model_pic= models.ImageField(upload_to=upload_image, default='blog/images/already.png')
    #
    #
    #
    # def upload_image(self, filename):
    #     return 'post/{}/{}'.format(self.name, filename)

     def __str__(self):
        return self.name



class ShopPage (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=3000)

    REQUIRED_FIELDS= ['product']


    def __str__(self):
        return self.product



class Gallerie (models.Model):
    picture= models.ForeignKey(Picture, on_delete=models.CASCADE)


class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    picture_upload= models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
    gallerie = models.ForeignKey(Gallerie, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class AboutU (models.Model):
    about = models.TextField(max_length=2000)
    get_to_know_us = models.TextField(max_length=3000)



class CartManager(models.Manager):
    def create_cart(self, total_price, number_of_products):
        if not name:
            raise ValueError('Product must have a name')


        product = self.model(name=name, description=description, price=price, product_image=product_image)


        product.save(using=self._db)

        return product


class Cart (models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_products = models.IntegerField()
    products = models.ArrayModelField(model_form_class= Product)
    #products = models.ManyToManyField(Product)


class ContactU (models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    how_can_i_help = models.TextField(max_length=3000)
    working_hours = models.TextField(max_length=3000)




class Store (models.Model):
    store_area = models.CharField(max_length=255)




class Brand (models.Model):
    brand_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()


    def __str__(self):
        return self.brand_name



class Categorie (models.Model):
    category_name = models.CharField(max_length=255)
    brands = models.ManyToManyField(Brand)


    def __str__(self):
        return self.category_name
