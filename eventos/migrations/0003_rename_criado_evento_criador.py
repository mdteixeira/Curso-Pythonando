# Generated by Django 4.2 on 2023-04-13 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_criado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='criado',
            new_name='criador',
        ),
    ]
