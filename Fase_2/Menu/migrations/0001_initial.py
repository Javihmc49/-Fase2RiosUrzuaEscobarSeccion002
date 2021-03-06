# Generated by Django 3.1.2 on 2020-10-27 02:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('promociones', models.CharField(max_length=100, null=True)),
                ('acompañamientos', models.CharField(max_length=100, null=True)),
                ('bebidas', models.CharField(max_length=50, null=True)),
                ('precio', models.IntegerField(max_length=15, null=True)),
            ],
        ),
    ]
