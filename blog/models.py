from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, blank=True)

    picture = ProcessedImageField(
        upload_to='my_category/images',
        default='/my_post/images/selfie.jpg',
        processors=[ResizeToFit(200, 113)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)

    picture = ProcessedImageField(
        upload_to='my_post/images',
        default='/my_post/images/selfie.jpg',
        processors=[ResizeToFit(1600, 900)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']
