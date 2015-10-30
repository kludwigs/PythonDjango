from django.shortcuts import render

# Create your views here.


# Create your views here.

from blog.models import MyBlog
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
		posts = MyBlog.objects.filter(published=True)
		return render(request, 'blog/index.html', {'posts': posts})

def details(request, slug):
	# get the Post object
	thepost = get_object_or_404(MyBlog, slug=slug)
	# now return the rendered template
	return render(request, 'blog/details.html', {'thepost': thepost})
	
def aboutme(request):
	return render(request, 'blog/aboutme.html')