from django.contrib import admin
from .models import Transaction, Day


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'borrower', 'book', 'date_requested', 'days', 'date_due', 'date_returned')
admin.site.register(Day)
