# Generated by Django 3.0.3 on 2020-05-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visual',
            name='id',
            field=models.AutoField(auto_created=True, default=4, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visual',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
