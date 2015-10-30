from django.db import models

# Create your models here.
class MyBlog(models.Model):
	title=models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content=models.TextField()
	published=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)

class PostComments(models.Model):
	content=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	#use the post itself as a key
	post = models.ForeignKey(MyBlog)
	
class Meta:
	ordering = ['=created']
	
	def __unicode__(self):
		return u'%s'%(self.title)
	def get_absolute_url(self):
		return reverse('blog.views.details',args=[self.slug])	
