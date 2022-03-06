import string
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .models import Shortener
from .forms import ShortenerForm

# Create your views here.
def create_shortened_url_view(request, suggestion=None, *args, **kwargs):
    initial_data = {}
    if suggestion:
        initial_data = {
            'shortened': suggestion,
        }
    shortener_form = ShortenerForm(request.POST or None, initial=initial_data)
    if shortener_form.is_valid():
        shortener_form.save()
        # shortener_form = ShortenerForm()
        return redirect(reverse("create-shortened-url"))
    else:
        print(shortener_form.errors)
    
    context = {
        "shortener_form": shortener_form,
    }
    return render(request, "shortener/shorten_url.html", context)

def redirect_from_shortened_url_view(request, shortened, *args, **kwargs):
    entry = get_object_or_404(Shortener, shortened=shortened)
    return redirect(entry.original)

def get_random_name(n):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))

def suggest_shortened_name_view(request, *args, **kwargs):
    suggestion = get_random_name(5)
    while Shortener.objects.filter(shortened=suggestion):
        suggestion = get_random_name(5)
    return create_shortened_url_view(request, suggestion=suggestion, *args, **kwargs)

class ShortenerListView(ListView):
    template_name = "shortener/shortener_list.html"
    queryset = Shortener.objects.all()
