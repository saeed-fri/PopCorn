from .forms import Users
from django.shortcuts import render


def register(request):
    # form = Users(request.POST)
    return render(request, "sign_up.html", {
        # 'form': form
        })


def forget(request):
    # form = Users(request.POST)
    return render(request, "forgot_password.html", {
        # 'form': form
        })


def post(request):
    # form = Users(request.POST)
    return render(request, "post.html", {
        # 'form': form
        })


def movie(request):
    # form = Users(request.POST)
    return render(request, "movie_profile.html", {
        # 'form': form
        })


def profile(request):
    # form = Users(request.POST)
    return render(request, "profile.html", {
        # 'form': form
        })


def related_user(request):
    # form = Users(request.POST)
    return render(request, "related_users.html", {
        # 'form': form
        })


def search(request):
    # form = Users(request.POST)
    return render(request, "search_results.html", {
        # 'form': form
        })


def sign_in(request):
    # form = Users(request.POST)
    return render(request, "sign_in.html", {
        # 'form': form
        })


def timeline(request):
    # form = Users(request.POST)
    return render(request, "timeline.html", {
        # 'form': form
        })


