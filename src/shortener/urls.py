from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_shortened_url_view, name="create-shortened-url"),
    path("<slug:shortened>/", views.redirect_from_shortened_url_view, name="redirection-from-shortened-url")
]