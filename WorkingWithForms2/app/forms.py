from django import forms
class UserForm(forms.Form):
    ch = ((1, 'Python'), (2, 'C'), (3, 'JavaScript'))
    name = forms.CharField(min_length=2, max_length=20, required=False, initial='Noname')
    password = forms.IntegerField(max_value=50, required=False, initial=45)
    # password = forms.IntegerField(max_value=50, required=False, widget=forms.PasswordInput)
    # age = forms.IntegerField(min_value=10, max_value=50, required=False)
    # agree = forms.BooleanField(label='Согласен на обработку персональных данных', required=False)
    # email = forms.EmailField(required=False)
    # url = forms.URLField(required=False)
    # file = forms.FileField(required=False)
    # photo = forms.ImageField(required=False)
    # date = forms.DateField(required=False)
    languages = forms.MultipleChoiceField(choices=ch)
    comment = forms.CharField(widget=forms.Textarea, label='Комментарий')
    field_order = ['languages', 'name']

class NewsForms(forms.Form):
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'main__input'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'main__textarea'}))
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ChoiceField(choices=((1, 'Спорт'), (2, 'Красота'), (3, 'Погода')), label='Категория')

class MakingAnOrder(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=False, initial='Noname', label='Имя')
    surname = forms.CharField(min_length=2, max_length=50, required=False, initial='Noname', label='Фамилия')
    email = forms.CharField(min_length=2, max_length=30,required=False, initial='None@none.nt', label='Email')
    address = forms.CharField(label='Страна', initial='Noname', required=False, max_length=25)
    address2 = forms.CharField(label='Регион', initial='Noname', required=False, max_length=50)
    address3 = forms.CharField(label='Город', initial='Noname', required=False, max_length=30)
    address4 = forms.CharField(label='Улица', initial='Noname', required=False, max_length=35)