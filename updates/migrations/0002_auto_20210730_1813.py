# Generated by Django 3.2.4 on 2021-07-30 21:13

from django.db import migrations, models
import updates.models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='descricao',
        ),
        migrations.AddField(
            model_name='update',
            name='imagem',
            field=models.ImageField(default='socialist-dog.jpg', upload_to=updates.models.upload_to),
        ),
    ]
