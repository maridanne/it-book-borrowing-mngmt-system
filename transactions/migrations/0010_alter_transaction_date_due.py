# Generated by Django 4.2 on 2023-05-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_alter_transaction_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_due',
            field=models.DateField(blank=True, null=True),
        ),
    ]
