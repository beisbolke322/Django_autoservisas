# Generated by Django 4.0.3 on 2022-03-20 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DarbuListas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Pavadink šitą darbąą kaip nors originaliai', max_length=100, verbose_name='Pavadinimas')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Darbo listas',
                'verbose_name_plural': 'Darbų listai',
            },
        ),
        migrations.CreateModel(
            name='DarboDuomenys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(help_text='Automobilio markė', max_length=30, verbose_name='A_marke')),
                ('modelis', models.CharField(help_text='Automobilio modelis', max_length=20, verbose_name='A_modelis')),
                ('sav', models.CharField(help_text='Automobilio savininko vardas, pavardė', max_length=70, verbose_name='A_sav')),
                ('suged', models.CharField(help_text='Automobilio sugedimai', max_length=200, verbose_name='A_sugedimai')),
                ('isCompleted', models.BooleanField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registracija.darbulistas')),
            ],
            options={
                'verbose_name': 'Darbo itemas',
                'verbose_name_plural': 'Darbo itemai',
            },
        ),
    ]
