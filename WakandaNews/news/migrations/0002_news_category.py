# Generated by Django 3.1.3 on 2020-11-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('lifestyle', 'Lifestyle'), ('sports', 'Sports'), ('travels', 'Travels'), ('skeping', 'Skeping'), ('fashion', 'Fashion'), ('night party', 'Night Party'), ('see beach', 'See Beach'), ('technology', 'Technology'), ('corporate', 'Corporate'), ('event time', 'Event Time'), ('politics', 'Politics')], max_length=100, null=True),
        ),
    ]
