from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from  .models import Post
from django.urls import reverse_lazy

class HomePageView(ListView):
    template_name='home.html'
    model= Post
    
class AboutPageView(TemplateView):
    template_name='about.html'
    
class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail.html"
    
class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields= ["title",'author','body']
    
class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title', 'body']
    
class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url= reverse_lazy("home")

# Create your views here.
