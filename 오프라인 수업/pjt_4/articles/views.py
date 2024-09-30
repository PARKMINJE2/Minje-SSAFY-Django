from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    # 모델클래스.objects.all()
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)