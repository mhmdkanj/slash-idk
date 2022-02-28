from django.shortcuts import render, redirect, get_object_or_404
from .models import Shortener

# Create your views here.
def create_shortened_url_view(request, *args, **kwargs):
    context = {}
    return render(request, "shorten_url.html", context)

def redirect_from_shortened_url_view(request, shortened, *args, **kwargs):
    entry = get_object_or_404(Shortener, shortened=shortened)
    return redirect(entry.original)
