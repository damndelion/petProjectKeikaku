from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from requests import Response
from django.http import JsonResponse

from .filters import AnimeFilter, MangaFilter
from .forms import NewUserForm, ReviewForm
from .models import Anime, Manga, ReviewAnime, ReviewManga, FavoriteAnime, FavoriteManga, Discussion, Comment


class IndexView(ListView):
    model = Anime
    paginate_by = 8
    context_object_name = 'animes'
    template_name = "home.html"
    ordering = ['popularity']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mangas'] = Manga.objects.filter().order_by('-rating')[:8]
        context['new_animes'] = Anime.objects.filter(aired__contains='2021').order_by('-popularity')[:8]
        context['comedy_mangas'] = Manga.objects.filter(genre__contains='comedy').order_by('-rating')[:8]
        return context


# Create your views here.
class AnimeView(ListView):
    model = Anime
    paginate_by = 24
    context_object_name = 'animes'
    template_name = 'anime_list.html'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AnimeFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AnimeFilter(self.request.GET, queryset=queryset).qs


class MangaView(ListView):
    model = Manga
    paginate_by = 24
    context_object_name = 'mangas'
    template_name = 'manga_list.html'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MangaFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return MangaFilter(self.request.GET, queryset=queryset).qs


class AnimeDetail(DetailView):
    model = Anime
    template_name = 'anime_detail.html'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ReviewAnime.objects.filter(anime=self.kwargs.get('pk')).order_by('-timestamp')[:5]
        favorite_animes = FavoriteAnime.objects.filter(user_id=self.request.user.id)
        anime_ids = favorite_animes.values_list('anime_id', flat=True)
        context['favorite'] = anime_ids
        return context


class MangaDetail(DetailView):
    model = Manga
    template_name = 'manga_detail.html'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ReviewManga.objects.filter(manga=self.kwargs.get('pk')).order_by('-timestamp')[:5]
        return context


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


@login_required(login_url='/login/')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        favorite_animes = FavoriteAnime.objects.filter(user_id=user_id)
        favorite_mangas = FavoriteManga.objects.filter(user_id=user_id)
        anime_ids = favorite_animes.values_list('anime_id', flat=True)
        manga_ids = favorite_mangas.values_list('manga_id', flat=True)
        anime_objects = Anime.objects.filter(id__in=anime_ids)
        manga_objects = Manga.objects.filter(id__in=manga_ids)
        context['favorites_anime'] = anime_objects
        context['favorites_manga'] = manga_objects
        return context


class SearchView(ListView):
    model = Anime
    template_name = 'search.html'
    context_object_name = 'animes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['animes'] = Anime.objects.filter(title__icontains=query)
        context['mangas'] = Manga.objects.filter(title__icontains=query) | \
                            Manga.objects.filter(alternativeTitle__icontains=query)

        return context


class ReviewCreateViewAnime(LoginRequiredMixin, CreateView):
    model = ReviewAnime
    fields = ['rating', 'content']
    template_name = 'anime_review.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.anime_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anime'] = get_object_or_404(Anime, id=self.kwargs['pk'])
        context['reviews'] = ReviewAnime.objects.filter(anime_id=self.kwargs['pk']).order_by('-timestamp')
        return context

    def get_success_url(self):
        return reverse_lazy('anime_detail', kwargs={'pk': self.object.anime.pk})


class ReviewDeleteViewAnime(DeleteView):
    model = ReviewAnime
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Review deleted successfully.')
        return super().form_valid(form)


class ReviewCreateViewManga(LoginRequiredMixin, CreateView):
    model = ReviewManga
    fields = ['rating', 'content']
    template_name = 'manga_review.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.manga_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manga'] = get_object_or_404(Manga, id=self.kwargs['pk'])
        context['reviews'] = ReviewManga.objects.filter(manga_id=self.kwargs['pk']).order_by('-timestamp')
        return context

    def get_success_url(self):
        return reverse_lazy('manga_detail', kwargs={'pk': self.object.manga.pk})


class ReviewDeleteViewManga(DeleteView):
    model = ReviewManga
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Review deleted successfully.')
        return super().form_valid(form)


def add_to_favorites_anime(request, pk):
    anime = Anime.objects.get(id=pk)
    current_user = request.user
    favorite_anime = FavoriteAnime.objects.create(user=current_user, anime=anime)
    return redirect('/profile/')


def remove_from_favorites_anime(request, pk):
    anime = Anime.objects.get(id=pk)
    current_user = request.user
    favorite_anime = FavoriteAnime.objects.filter(user=current_user, anime=anime).delete()
    return redirect('/profile/')


def add_to_favorites_manga(request, pk):
    manga = Manga.objects.get(id=pk)
    current_user = request.user
    favorite_anime = FavoriteManga.objects.create(user=current_user, manga=manga)
    return redirect('/profile/')


def remove_from_favorites_manga(request, pk):
    manga = Manga.objects.get(id=pk)
    current_user = request.user
    favorite_anime = FavoriteManga.objects.filter(user=current_user, manga=manga).delete()
    return redirect('/profile/')


class ForumView(ListView):
    model = Discussion
    paginate_by = 10
    context_object_name = 'discussions'
    template_name = "forum.html"
    ordering = ['date_created']



class DiscussionView(DetailView):
    model = Discussion
    template_name = 'discussion.html'
    context_object_name = 'discussion'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'discussion.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.discussion_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_success_url(self):
        return reverse_lazy('discussion', kwargs={'pk': self.object.discussion.pk})


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '/forum/'

    def form_valid(self, form):
        messages.success(self.request, 'Review deleted successfully.')
        return super().form_valid(form)

