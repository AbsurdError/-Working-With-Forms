from django.urls import path
from .views import index, myForm, news, appointment, order
urlpatterns = [
    path('', index, name='home'),
    path('myform', myForm, name='form'),
    path('news', news, name='news'),
    path('appointment', appointment, name='appointment'),
    path('order', order, name='order'),
    # path('user', user, name='user'),
]