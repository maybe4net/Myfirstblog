from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Blogpost
from .forms import BlogpostForm


# Create your views here.
def index(request):
    """Отображение всех тем"""
    posts = Blogpost.objects.order_by('date_added')

    context = {'blogposts': posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post_view(request):
    """Создание нового поста"""
    if request.method != 'POST':
        form = BlogpostForm()
    else:
        form = BlogpostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Редактирование поста"""
    post = Blogpost.objects.get(id=post_id)

    # Проверка владельца поста
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogpostForm(instance=post)
    else:
        form = BlogpostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)
