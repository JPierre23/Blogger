from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment, Blog, Tags
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def blog_index(request):
    blog = Blog.objects.all()
    return render(request,'blog/index.html',{'blog':blog})

def blog_detail(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    # unused_tags=Tags.objects.exclude(id__in =blog.tags.all().values_list('id'))
    return render(request,'blog/detail.html',{
        'blog':blog,
        # 'unused_tags':unused_tags,
        
        })

class BlogCreate(CreateView):
    model=Blog
    fields={'title','img','info'}
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class BlogUpdate(UpdateView):
    model=Blog
    fields=['title','img']
    success_url='/blog/'

class BlogDelete(DeleteView):
    model=Blog
    success_url='/'

# def tag_detail():
#     tags= Tags.objects.all()
#     return render(request,)
# def add_tag():

# class TagCreate():

