# Generated by Django 3.1.2 on 2021-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(choices=[('Cakes', 'Cakes'), ('Bouquets', 'Gifts'), ('Chocolates', 'Chocolates'), ('Plants', 'Plants')], max_length=100, null=True)),
                ('item_image', models.ImageField(null=True, upload_to='item_img')),
            ],
        ),
    ]