# Generated by Django 5.0.4 on 2024-04-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='companies',
            field=models.TextField(default='data intelligence'),
            preserve_default=False,
        ),
    ]
