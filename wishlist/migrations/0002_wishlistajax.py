# Generated by Django 4.1 on 2022-10-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlistajax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=50)),
                ('harga_barang', models.IntegerField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]