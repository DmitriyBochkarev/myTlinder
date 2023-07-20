from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, MatchCreateForm
from .models import Profile, Friendship
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
)
from django.forms import inlineformset_factory


def about(request):
    return render(request, 'users/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    instance = request.user
    profile = Profile.objects.filter(user=instance)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile_update.html', context)


def index(request):
    all_users = User.objects.all()
    return render(request, 'users/index.html', {'all_users': all_users})


def match(request):
    instance = request.user.profile
    matches = Friendship.objects.filter(from_friend=instance)
    matches_to_me = Friendship.objects.filter(to_friend=instance)
    return render(request, 'users/match.html', {'matches': matches, 'matches_to_me': matches_to_me})


# def match_create(request, **kwargs):
#     if request.method == 'POST':
#         matchform = MatchCreateForm(request.POST, instance=request.user)
#
#         if matchform.is_valid():
#             matchform.save()
#
#             messages.success(request, f'Ваш профиль успешно обновлен.')
#             return redirect('match')
#
#     else:
#         matchform = MatchCreateForm(instance=request.user)
#
#     context = {
#         'matchform': matchform,
#
#     }
#
#     return render(request, 'users/match_create.html', context)




# def match_create(request, **kwargs):
#     author = Profile.objects.get(pk=request.user.id)
#     other = Profile.objects.get(**kwargs)
#     FriendshipInlineFormSet = inlineformset_factory(Profile, Friendship, fk_name='from_friend', fields=["to_friend"])
#     if request.method == "POST":
#         formset = FriendshipInlineFormSet(request.POST, instance=author, **kwargs)
#         if formset.is_valid():
#             formset.save()
#             messages.success(request, f'Ваш профиль успешно обновлен.')
#             return redirect('match')
#     else:
#         formset = FriendshipInlineFormSet(instance=author, **kwargs)
#     return render(request, "users/match_create.html", {"formset": formset})


def match_create(request, **kwargs):
    author = Profile.objects.get(pk=request.user.id)
    other = Profile.objects.get(**kwargs)
    if request.method == "POST":
        matchform = Friendship(from_friend=author, to_friend=other)
        if Friendship.objects.filter(to_friend=author, from_friend=other) and Friendship.objects.filter(to_friend=other, from_friend=author):
            messages.success(request, f'У вас уже есть мэтч с {other}.')

            messages.success(request, f'Email: {other.user.email}. ')
            return redirect('match')
        else:
            matchform.save()

            if Friendship.objects.filter(to_friend=author, from_friend=other):
                messages.success(request, f'Поздравляем, у вас мэтч с {other}. ')
                instance = request.user
                profile = Profile.objects.filter(user=instance)
                messages.success(request, f'Email {other.user.email}. ')
            else:
                messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('match')

    matchform = MatchCreateForm(request.POST)
    return render(request, "users/match_create.html")