from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, RedirectView
from .forms import ShortenUrlForm
from .models import Url
import pyshorteners

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenUrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = pyshorteners.Shortener().tinyurl.short(original_url)
            return render(request, 'main/shorten_url.html', {'form': form, 'short_url': shortened_url})
    else:
        form = ShortenUrlForm()
    return render(request, 'main/shorten_url.html', {'form': form})

def redirect_short_url(request, short_url):
    url = Url.objects.get(shortened_url=short_url)
    return redirect(url.original_url)