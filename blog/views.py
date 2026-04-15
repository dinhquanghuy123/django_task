from django.http import HttpResponse
from django.template import loader
from .models import blog

# Create your views here.


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def blog_views(request):
    blogs = blog.objects.all().values()
    template = loader.get_template('blog.html')
    context = {
        'blogs': blogs,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    myblog = blog.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'myblog': myblog,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    mydata = blog.objects.all().values_list('firstname')
    template = loader.get_template('template.html')
    context = {
        'fruits': mydata,
    }
    return HttpResponse(template.render(context, request))
