# Generated by Django 5.0.3 on 2024-03-29 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_content_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='previous_version',
        ),
        migrations.RemoveField(
            model_name='content',
            name='version',
        ),
    ]