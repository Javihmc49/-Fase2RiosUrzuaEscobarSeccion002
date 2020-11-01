# Generated by Django 3.1.2 on 2020-11-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_auto_20201026_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('motivo', models.CharField(choices=[('VentadePizzas', 'Freshman'), ('EventosCorporativos', 'Sophomore'), ('Alianzas', 'Junior'), ('ProblemasConTuPedido', 'Senior'), ('Comentarios', 'Graduate')], max_length=100)),
            ],
        ),
    ]