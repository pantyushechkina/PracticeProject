from django.db import models


class Contact(models.Model):
    name = models.CharField('Name', max_length=100)
    position = models.TextField('Position')
    phone = models.CharField('Phone number', max_length=20)
    email = models.CharField('Email', max_length=40)

    def __str__(self):
        return self.name


class TypeProduct(models.Model):
    idType = models.IntegerField('Id')
    typeName = models.CharField('Type of product', max_length=20)

    def __str__(self):
        return self.typeName


class Product(models.Model):
    idType = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=30)
    VendorCode = models.CharField('Vendor code', max_length=13)


    def __str__(self):
        return self.VendorCode


class Item(models.Model):
    idType = models.IntegerField('Id')
    Name = models.CharField('Name', max_length=30)
    VendorCode = models.CharField('Vendor code', max_length=13)
    ImgURL = models.CharField('Img URL', max_length=100)

    def __str__(self):
        return self.VendorCode