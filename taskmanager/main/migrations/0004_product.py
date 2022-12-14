# Generated by Django 4.0.6 on 2022-09-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_typeproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idType', models.IntegerField(verbose_name='Id')),
                ('Name', models.CharField(max_length=30, verbose_name='Name')),
                ('VendorCode', models.CharField(max_length=13, verbose_name='Vendor code')),
                ('ImgURL', models.CharField(max_length=100, verbose_name='Img URL')),
            ],
        ),
    ]
