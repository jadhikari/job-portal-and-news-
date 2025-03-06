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
    
    def get_translated_field(self, field_base_name):
        lang = get_language()
        field_name = f"{field_base_name}_{lang}"
        # Attempt to get the field in the current language
        if hasattr(self, field_name):
            value = getattr(self, field_name)
            if value:
                return value
        # Fallback to English if available
        field_name_en = f"{field_base_name}_en"
        if hasattr(self, field_name_en):
            value = getattr(self, field_name_en)
            if value:
                return value
        # Fallback to Japanese as the default
        field_name_ja = f"{field_base_name}_ja"
        if hasattr(self, field_name_ja):
            return getattr(self, field_name_ja)
        return None

class News(BaseModel):
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = RichTextField()
    content_en = RichTextField(blank=True, null=True)
    content_ne = RichTextField(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('header')
    
    def get_translated_content(self):
        return self.get_translated_field('content')

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

    def get_translated_header(self):
        return self.get_translated_field('header')
    
    def get_translated_content(self):
        return self.get_translated_field('content')

    def __str__(self):
        return self.get_translated_header()

class Video(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField()

    def get_translated_header(self):
        return self.get_translated_field('header')

    def __str__(self):
        return self.get_translated_header()
    
class Job(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    attract_point_ja = models.CharField(max_length=255)
    attract_point_en = models.CharField(max_length=255, blank=True, null=True)
    attract_point_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = RichTextField()
    content_en = RichTextField(blank=True, null=True)
    content_ne = RichTextField(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('header')

    def get_translated_attract_point(self):
        return self.get_translated_field('attract_point')

    def get_translated_content(self):
        return self.get_translated_field('content')

    def __str__(self):
        return self.get_translated_header()



class TeamMember(BaseModel):
    name_ja = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    position_ja = models.CharField(max_length=100)
    position_en = models.CharField(max_length=100)
    position_ne = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    blog_ja = RichTextField(blank=True, null=True)
    blog_en = RichTextField(blank=True, null=True)
    blog_ne = RichTextField(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('name')
    
    def get_translated_position(self):
        return self.get_translated_field('position')
    
    def get_translated_content(self):
        return self.get_translated_field('blog')

    def __str__(self):
        return self.get_translated_header()
