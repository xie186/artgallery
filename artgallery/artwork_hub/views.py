from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Artwork

class Index(ListView):
    models = Artwork
    template_name = "index.html"
    def get_queryset(self):
        """Return the last five published questions."""
        return Artwork.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['nav_status_home'] = "active"
        return context 
