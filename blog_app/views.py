from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import CreateView
from  .models import Post

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

# Create your views here.
