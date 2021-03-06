# Generated by Django 4.0.5 on 2022-07-04 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('info_contato', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'Aberta'), ('F', 'Finalizada')], default='A', max_length=1)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.cidade')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.uf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
