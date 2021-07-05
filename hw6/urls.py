from django.urls import path

from hw6 import views

urlpatterns = [
    path("news/", views.NewsView.as_view()),
    path("news/<int:pk>/", views.NewsViewItem.as_view()),
    path("laws/", views.LawView.as_view()),
    path("laws/<int:pk>/", views.LawView.as_view()),
    path("publication/", views.PublicationView.as_view()),
    path("publication/<int:pk>/", views.PublicationView.as_view()),
    path("favourite/", views.FavouriteView.as_view()),
]