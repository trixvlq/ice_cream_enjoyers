from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Prefetch
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import *
from .forms import *


def index(request):
    icecreams = IceCream.objects.all()
    context = {
        'icecreams': icecreams,
        'set': 'Главная страница',
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context)


def icecream(request, slug):
    ice = IceCream.objects.get(slug=slug)
    user = request.user
    if ice.user == user:
        context = {
            'icecream': ice,
            'title': ice.title,
            'creator':True
        }
    else:
        context = {
            'icecream': ice,
            'title': ice.title
        }
    return render(request, 'icecream.html', context)


def search(request):
    info = request.POST.get('search')
    info = info.lower()
    if info:
        ice = IceCream.objects.filter(title__icontains=info)
        if ice:
            context = {
                'icecreams': ice,
                'set': 'Результаты поиска',
                'title': 'Поиск'
            }
        else:
            context = {
                'set': 'Ничего не найдено',
                'title': 'Поиск'
            }
    return render(request, 'index.html', context)


@login_required
def favorite(request, slug):
    user = request.user
    ice = get_object_or_404(IceCream, slug=slug)
    bag, created = Bag.objects.get_or_create(user=user)
    if created or ice not in bag.items.all():
        bag.items.add(ice)
        ice.saves += 1
        bag.save()
    else:
        pass
    return redirect('home')


def trending(request):
    ice = IceCream.objects.all().order_by('saves')
    context = {
        'icecreams': ice,
        'set': 'Популярные',
        'title': 'Популярное'
    }
    return render(request, 'index.html', context)


@login_required()
def add_ice(request):
    if request.method == "POST":
        form = IceCreamForm(request.POST, request.FILES)
        if form.is_valid():
            ice_cream = form.save(commit=False)
            ice_cream.user = request.user

            ice_cream.save()
            return redirect('home')
    else:
        form = IceCreamForm
        return render(request, 'create_ice_cream.html', {'title': 'Создать мороженное', 'form': form})


@login_required()
def favorites(request):
    user = request.user
    icecreams = Bag.objects.prefetch_related(
        Prefetch(
            'items',
            queryset=IceCream.objects.all()
        )
    ).get(user=user)
    icecreams = icecreams.items.all()
    return render(request, 'index.html',
                  {'set': f'Любимое мороженое пользователя {user.username}', 'icecreams': icecreams,
                   'title': 'Любимые мороженые'})


@login_required()
def my_ice_creams(request):
    user = request.user
    icecreams = IceCream.objects.filter(user=user)
    return render(request, 'index.html', {'title': 'Мои мороженые', 'set': 'Мои мороженые', 'icecreams': icecreams})


@login_required()
def delete_ice_cream(request,slug):
    ice = IceCream.objects.get(slug=slug)
    ice.delete()
    return redirect('home')

@login_required()
def change_ice_cream(request,slug):
    ice = IceCream.objects.get(slug=slug)
    if ice.user != request.user:
        return HttpResponseForbidden("You don't have permission to update this ice cream.")

    if request.method == "POST":
        form = IceCreamForm(request.POST, request.FILES, instance=ice)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IceCreamForm(instance=ice)
    return render(request,'change_ice_cream.html', {'form': form,'icecream':ice})
