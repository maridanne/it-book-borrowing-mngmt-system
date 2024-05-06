# Generated by Django 4.2 on 2023-05-04 03:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_remove_borrowrequest_date_accepted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrequest',
            name='date_accepted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='date_borrowed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='date_cancelled',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='date_denied',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='date_due',
            field=models.DateTimeField(blank=True, help_text='Date for due', null=True),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='date_requested',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]