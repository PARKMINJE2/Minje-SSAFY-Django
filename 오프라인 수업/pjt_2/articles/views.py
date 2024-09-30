from django.shortcuts import render

# Create your views here.
def index(request):
    # context는 딕셔너리 구조
    # templates에서 {{ name }} context의 key의 value값을 사용할 수 있다.
    context = {
        'name' : 'Tom hardy',
        'number' : 1,
    }
    # 항상 render함수의 3번 째 항목에는 매개변수(context)
    return render(request, 'articles/index.html', context)

import random

def dinner(request):
    foods = ['족발', '치킨', '피자', '보쌈', '냉모밀', '아란치니']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # message= request.GET['message']
    text = request.GET.get('throw')
    context = {
        'talk' : text,
        
    }
    return render(request, 'articles/catch.html', context)

def detail(request, number):
    context = {
        'num' : number
    }
    return render(request, 'articles/detail.html', context)