# Generated by Django 4.2 on 2023-05-07 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import transactions.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_book_image'),
        ('transactions', '0005_borrowrequest_date_accepted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(default=transactions.models.generate_transaction_id, max_length=8, unique=True)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('date_returned', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.days')),
            ],
        ),
        migrations.DeleteModel(
            name='BorrowRequest',
        ),
        migrations.DeleteModel(
            name='TransactionStatus',
        ),
    ]
