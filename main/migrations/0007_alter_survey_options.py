# Generated by Django 5.0.4 on 2024-05-03 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_bio_question_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['id'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
    ]
