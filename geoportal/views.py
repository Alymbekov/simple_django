from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import WorldBorder, Post, Tag, Comment


class CitiesListView(ListView):
    template_name = 'cities/city-list.html'
    model = WorldBorder


class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = WorldBorder


def index(request):
    return render(request, 'index.html', {})


def post_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query)| Q(body__icontains=search_query))

    else:
        posts = Post.objects.all()[::-1]

    paginator = Paginator(posts,1)

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previus_url = '?page={}'.format(page.previous_page_number())
    else:
        previus_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object':page,
        'is_paginated':is_paginated,
        'next_url': next_url,
        'previus_url':previus_url
    }

    return render(request, 'blog.html', context=context)


def search(request):
    return render(request, 'archives.html', {})


class PostDetailView(DetailView):
    template_name = 'blog-single.html'
    model = Post

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, context={'objects': obj})


class TagListView(ListView):
    template_name = 'blog.html'
    model = Tag

    def get(self, request):
        tag = get_object_or_404(self.model)
        return render(request, self.template_name, context={'tags': tag})


def maps(request):
    obj = Post.objects.get(pk=2)
    print(obj.latitude, obj.longitude)
    return render(request, 'blog.html', {'object': obj})


def about(request):
    return render(request, 'portfolio.html', {})


def contact(request):
    return render(request, 'contact.html', {})



class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('cities:blog-post')

    fields = [
        'owner', 'title', 'description',
        'place_name', 'latitude', 'longitude',
        'tags'
    ]


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    success_url = reverse_lazy('cities:blog-post')

    fields = [
        'owner', 'title', 'description',
        'place_name', 'latitude', 'longitude',
        'tags'
    ]


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
