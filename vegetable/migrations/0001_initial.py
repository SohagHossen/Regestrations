# Generated by Django 5.0.6 on 2024-06-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_name', models.CharField(max_length=50)),
                ('rec_price', models.IntegerField()),
                ('rec_dis', models.TextField()),
                ('rec_image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
