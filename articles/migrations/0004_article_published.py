# Generated by Django 3.2.9 on 2021-11-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211120_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
