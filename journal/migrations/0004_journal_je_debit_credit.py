# Generated by Django 4.1 on 2022-08-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_rename_je_type_journal_je_entry_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='je_debit_credit',
            field=models.CharField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]
