from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('anime/', views.AnimeView.as_view(), name="anime_list"),
    path('manga/', views.MangaView.as_view(), name="manga_list"),
    path('anime/<int:pk>/', views.AnimeDetail.as_view(), name="anime_detail"),
    path('manga/<int:pk>', views.MangaDetail.as_view(), name="manga_detail"),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('search/', views.SearchView.as_view(), name='search'),
    path('anime/<int:pk>/review/', views.ReviewCreateViewAnime.as_view(), name='review_create_anime'),
    path('anime/delete/<int:pk>/', views.ReviewDeleteViewAnime.as_view(), name='review_delete_anime'),
    path('manga/<int:pk>/review/', views.ReviewCreateViewManga.as_view(), name='review_create_manga'),
    path('manga/delete/<int:pk>/', views.ReviewDeleteViewManga.as_view(), name='review_delete_manga'),
    path('anime/<int:pk>/favorite', views.add_to_favorites_anime, name="add_to_favorites_anime"),
    path('anime/<int:pk>/favorite/delete', views.remove_from_favorites_anime, name="remove_from_favorites_anime"),
    path('manga/<int:pk>/favorite', views.add_to_favorites_manga, name="add_to_favorites_manga"),
    path('manga/<int:pk>/favorite/delete', views.remove_from_favorites_manga, name="remove_from_favorites_manga"),
    path('forum/', views.ForumView.as_view(), name='forum'),
    path('discussion/<int:pk>/', views.DiscussionView.as_view(), name='discussion'),
    path('discussion/<int:pk>/add_comment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('discussion/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]




