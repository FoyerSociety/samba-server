# Generated by Django 2.2.7 on 2019-11-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]