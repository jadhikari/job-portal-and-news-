import random
import string
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.translation import get_language

def generate_random_id():
    """Generates a random 6-character alphanumeric string."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class BaseModel(models.Model):
    unique_id = models.CharField(max_length=6, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_random_id()
            # Ensure the generated ID is unique for the model.
            ModelClass = self.__class__
            while ModelClass.objects.filter(unique_id=self.unique_id).exists():
                self.unique_id = generate_random_id()
        super().save(*args, **kwargs)

class News(BaseModel):
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = RichTextField()
    content_en = RichTextField(blank=True, null=True)
    content_ne = RichTextField(blank=True, null=True)

    def get_translated_header(self):
        lang = get_language()
        if lang == "ja":
            return self.header_ja
        elif lang == "ne":
            return self.header_ne
        return self.header_en if self.header_en else self.header_ja  # Default to English

    def get_translated_content(self):
        lang = get_language()
        if lang == "ja":
            return self.content_ja
        elif lang == "ne":
            return self.content_ne
        return self.content_en if self.content_en else self.content_ja  # Default to English

    def __str__(self):
        return self.get_translated_header()

class Blog(BaseModel):
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = RichTextField()
    content_en = RichTextField(blank=True, null=True)
    content_ne = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.header_ja

class Video(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.header_ja

class Job(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = RichTextField()
    content_en = RichTextField(blank=True, null=True)
    content_ne = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.header_ja
