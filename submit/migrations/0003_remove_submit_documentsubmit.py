# Generated by Django 4.0.2 on 2022-05-04 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0002_remove_submit_document_submit_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='documentSubmit',
        ),
    ]
