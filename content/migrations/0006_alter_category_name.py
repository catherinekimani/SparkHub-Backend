# Generated by Django 5.0.3 on 2024-03-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_content_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('FOOD', 'Food'), ('ART', 'Art'), ('TECH', 'Tech'), ('FASHION', 'Fashion'), ('HEALTH', 'Health & Wellness')], max_length=50),
        ),
    ]
