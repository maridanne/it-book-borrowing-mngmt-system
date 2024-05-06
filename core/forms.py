from django.forms import ModelForm
from books.models import Book, Category
from transactions.models import Transaction
from django.forms import DateInput
from userprofiles.models import Profile


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'borrower', 'book', 'days']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'description', 'image']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class DateInput(DateInput):
    input_type = 'date'

class UpdateTransactionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transaction_id'].disabled = True
        self.fields['borrower'].disabled = True
        self.fields['book'].disabled = True
        self.fields['days'].disabled = True

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'borrower', 'book', 'days', 'date_due']
        widgets = {
            'date_due': DateInput(),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['student_id', 'course', 'year', 'profile_pic']
