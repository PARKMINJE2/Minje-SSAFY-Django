from django.urls import path
from . import views

# URL 네임 스페이스(유지보수 용이)
# {% url 'articles:index' %}
app_name = "articles"

# name = "index" --> naming url patterns
# 직접 href = "/index/" 이렇게 하드코딩 하지 않고 name 으로 참조
# {% url 'articles:index' %}

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('dinner/', views.dinner , name='dinner'),
    
    path('search/', views.search, name='search'),
    
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    
    path('<int:num>/', views.detail , name='detail'),
]
