from django.forms import ModelForm
from apps.books.models import Book, Category
from apps.account.models import User

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','quantity_pages','book_cover','status_book','note','year','price','quantity','synopsis','publishing_company','category']
        
    def init(self, args, **kwargs):
        super(BookForm, self).init(args, **kwargs)
        print('mulher bonita')
        self.user = kwargs['initial']['user']

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'