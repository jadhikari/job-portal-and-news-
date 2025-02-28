from django.contrib import admin
from .models import News, Blog, Video, Job

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('unique_id','header_ja', 'header_en', 'created_at', 'user')
    search_fields = ('unique_id', 'header_en')
    readonly_fields = ('unique_id', 'created_at', 'updated_at')
    # Exclude the 'user' field so it's not visible in the form
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        # If this is a new object, set the user to the currently logged-in admin user.
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(News)
class NewsAdmin(BaseModelAdmin):
    pass  

@admin.register(Blog)
class BlogAdmin(BaseModelAdmin):  
    pass
    
@admin.register(Video)
class VideoAdmin(BaseModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(BaseModelAdmin):
    pass