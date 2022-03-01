from django.shortcuts import render, redirect, get_object_or_404
from .models import Shortener
from .forms import ShortenerForm

# Create your views here.
def create_shortened_url_view(request, *args, **kwargs):
    shortener_form = ShortenerForm(request.POST or None)
    if shortener_form.is_valid():
        shortener_form.save()
        shortener_form = ShortenerForm()
    else:
        print(shortener_form.errors)
    
    context = {
        "shortener_form": shortener_form,
    }
    return render(request, "shortener/shorten_url.html", context)

def redirect_from_shortened_url_view(request, shortened, *args, **kwargs):
    entry = get_object_or_404(Shortener, shortened=shortened)
    return redirect(entry.original)
