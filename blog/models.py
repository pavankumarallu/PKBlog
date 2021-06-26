from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
    	return self.title

    

class Post(models.Model):
    title = models.CharField(max_length = 100)
    overview = models.TextField()
    short_name = models.CharField(max_length = 50,null = True,blank = True)
    body_text = RichTextUploadingField(null = True)
    slug = models.SlugField(null=True, blank=True)
    time_upload = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField(upload_to = 'thumbnails')
    categories = models.ManyToManyField(Category)
    
    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)
        
     

        
    	
 
    
    
    
    
    
	
 
    
    

	
	
	
	
 
	
 
	

	
	
 
 
	
	
		
		
	
	
	
	

	
	
    
    
    
    
	

    

	
	
	