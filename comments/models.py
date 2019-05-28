from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Comment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    # text = models.TextField()
    text = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time']
