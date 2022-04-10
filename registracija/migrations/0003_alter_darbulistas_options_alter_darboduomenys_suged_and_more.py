# Generated by Django 4.0.3 on 2022-04-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registracija', '0002_alter_darbulistas_options_alter_darbulistas_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='darbulistas',
            options={'verbose_name': 'Darbu listas', 'verbose_name_plural': 'Darbu listai'},
        ),
        migrations.AlterField(
            model_name='darboduomenys',
            name='suged',
            field=models.CharField(help_text='Automobilio sugedimai/pakeitimai', max_length=200, verbose_name='A_sugedimai'),
        ),
        migrations.AlterField(
            model_name='darbulistas',
            name='title',
            field=models.CharField(help_text='Pavadink šitą darbų seką kaip nors originaliai', max_length=100, verbose_name='Pavadinimas'),
        ),
    ]
