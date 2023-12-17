from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, NewsForms, MakingAnOrder
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'<h2>Привет, {name}, твой возраст: {age}</h2>')
    else:
        form = UserForm()
        return render(request, 'App/index.html', context={'form': form})

def news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        category = request.POST.get('category')
        return HttpResponse(f'<h2>Новость {title}<br>'
                            f'Контент {content}<br>'
                            f'Категория {category}, {is_published}</h2>')
    else:
        formNews = NewsForms()
        return render(request, 'App/news.html', context={'formNews': formNews})

def myForm(request):
    return render(request, 'App/form.html')

def appointment(request):
    if request.method == "POST":
        name = request.POST.get('name', 'Unverifed')
        email = request.POST.get('email', 'Unverifed')
        phone = request.POST.get('phone', 'Unverifed')
        service = request.POST.get('service', 'Unverifed')
        car_info = request.POST.get('car_info', 'Unverifed')

        data = {"name": name, 'email': email, 'phone': phone, 'service': service, 'car_info': car_info}

        return render(request, 'app/return.html', context={'info': data})

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        address3 = request.POST.get('address3')
        address4 = request.POST.get('address4')
        return HttpResponse(f'<h2>{name} {surname}, проверьте адрес доставки:<br>{address}<br>{address2}<br>{address3}<br>{address4}</h2>')
    else:
        orders = MakingAnOrder()
        return render(request, 'app/order.html', context={'orders': orders})