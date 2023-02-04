from django.forms import ModelForm, Select, ChoiceField
from books.models import Book, Category
from account.models import User

class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs) 
           
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        
    class Meta:
        model = Book
        fields = [
            'name',
            'quantity_pages',
            'book_cover',
            'status_book',
            'author',
            'note',
            'year',
            'price',
            'quantity',
            'synopsis',
            'publishing_company',
            'category',
            ]
        
        widgets = {
            'status_book': Select(attrs={'class': 'form-select'}),
            'typeCategoria': Select(attrs={'class': 'form-select'}),
        }