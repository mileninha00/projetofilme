from django.shortcuts import render
from django.urls import reverse_lazy
from filme.forms import FilmeForm, PlaylistForm
from .models import Filme, Playlist
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
    context_object_name= 'playlists'
    paginate_by = 5
    queryset=Playlist.objects.order_by('-id')

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist/playlist_detail.html'

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['nome', 'filmes']
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist_list')

class FilmeListView(ListView):
    model = Filme
    template_name = 'filme/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name ='filme/filme_form.html'
    success_url=reverse_lazy('filme_list')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name ='filme/filme_form.html'
    success_url = reverse_lazy('filme_list')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme/filme_confirm_delete.html'
    success_url= reverse_lazy('filme_list')