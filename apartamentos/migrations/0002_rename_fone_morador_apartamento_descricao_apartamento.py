# Generated by Django 3.2.7 on 2021-09-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartamentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartamento',
            old_name='fone_morador',
            new_name='descricao_apartamento',
        ),
    ]
