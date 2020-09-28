# Generated by Django 3.0.9 on 2020-09-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['ordering', 'title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
