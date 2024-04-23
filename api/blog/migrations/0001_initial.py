# Generated by Django 5.0.4 on 2024-04-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('exerpt', models.TextField(max_length=200)),
                ('content', models.TextField()),
                ('publishedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
