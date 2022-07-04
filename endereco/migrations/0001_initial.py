# Generated by Django 4.0.5 on 2022-07-04 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=255)),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.uf')),
            ],
        ),
    ]
