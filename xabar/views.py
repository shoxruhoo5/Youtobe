from django.shortcuts import render, redirect
from .forms import *

def home(request):
    r = News.objects.all()
    if request.POST:
        news_id = request.POST['one']
        one_news = News.objects.get(id=news_id)
        if request.user in one_news.likes.all():
            one_news.likes.remove(request.user)
        else:
            one_news.likes.add(request.user)
    return render(request, 'home.html',  {'yangiliklar': r})
    
def category(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home',)
    return render(request, 'create.html', {'form':form})

def user(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            parol = form.cleaned_data['password']
            user.set_password(parol)
            user.save()
            return redirect('home',)
    return render(request, 'create.html', {'form':form})

def news(request):
    form = NewsForm()
    if request.POST:
        form = NewsForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home',)
    return render(request, 'create.html', {'form':form})

def detail(request, id):
    form = CommentForm()
    one = News.objects.get(id=id)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            c1 = form.save(commit=False)
            c1.news = one
            c1.muallif = request.user
            c1.save()
            return redirect('detail' , one.id)
    context = {
        'one': one,
        'com': form
    }
    return render(request, 'detail.html', context)

def news(request):
    form = NewsForm()
    if request.POST:
        form = NewsForm(request.POST, files = request.FILES)
        if form.is_valid():
            news_create = form.save()
            news_create.author = request.user
            news_create.save()
            return redirect('home')
    return render(request,'create.html',{'form':form})

