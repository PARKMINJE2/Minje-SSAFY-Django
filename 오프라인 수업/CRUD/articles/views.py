from django.shortcuts import render, redirect

# Create your views here.

# 현재 디렉토리의 models.py로부터 Article 모델을 가져오겠다.
from .models import Article

def index(request):
  # QuerySet API ---> 전체 데이터 조회 : Aritlce.objects.all()
  articles = Article.objects.all()

  context = {
    'articles' : articles,
  }
 
  return render(request, 'articles/index.html', context)

# 단일 게시글 페이지 렌더링 
def detail(request, pk):
  # QuerySet API ---> 단일 데이터 조회 : get
  article = Article.objects.get(pk = pk)
  context = {
    'article' : article,
  }

  return render(request, 'articles/detail.html', context)

# 페이지 렌더링
def new(request):
  return render(request, 'articles/new.html')


# render와 redirect차이
# render : 사용자에게 새로운 페이지를 보여줄 때 사용
# redirect : 데이터 처리 후 다른 페이지로 이동 할때 사용

# 페이지 리다이렉트(데이터를 받아서 DB에 저장 - POST방식)
def create(request):
  # Create 2번, 3번방법 절대 x
  # GET방식은 데이터가 url에 노출 ---> 데이터를 조회, 검색
  # POST방식은 보안성(csrf 토큰) ---> 데이터를 생성, 수정, 삭제

  title = request.POST.get('title')
  content = request.POST.get('content')

  # 저장 ---> 2번 방법(코드가 간결하면서 안정성)
  article = Article(title = title, content = content)
  # 데이터 관리(저장) 원칙 : 안정성
  # save하기전에 유효성 검사!!
  article.save()

  # 게시글을 생성(데이터가 변경됐다)하고, 생성버튼 누르고 어떤 페이지로 이동할건가??
  # 클라이언트가 GET 요청을 한번 더 보내도록 한다(redirect).
  # 데이터가 변경 되었을 때 경로에 요청
  return redirect('articles:detail', article.pk)


# 단일 게시글 조회 후 삭제 
# 데이터 변경 ---> redirect
def delete(request, pk):
  article = Article.objects.get(pk = pk)
  article.delete()
  # 여기서 request는 무슨 방식일까? POST방식 왜?(DB 변경)
  return redirect('articles:index')

# 페이지 렌더링(create와 차이 : 기존에 있던 게시글을 조회)
def edit(request, pk):
  article = Article.objects.get(pk = pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/edit.html', context)

# 페이지 리다이렉트(create와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
  article = Article.objects.get(pk = pk)

  article.title = request.POST.get('title')
  article.content = request.POST.get('content')

  article.save()

  return redirect('articles:detail', article.pk)

