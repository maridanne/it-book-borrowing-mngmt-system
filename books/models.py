from django.db import models
from django.utils.text import slugify 

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/book_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
