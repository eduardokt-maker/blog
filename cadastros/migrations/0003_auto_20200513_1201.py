# Generated by Django 3.0.6 on 2020-05-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_pessoas_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='codigo',
            field=models.AutoField(max_length=5, primary_key=True, serialize=False),
        ),
    ]