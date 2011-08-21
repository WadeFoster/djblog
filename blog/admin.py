from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'status', 'body_markdown', 'pub_date', 'body_html')
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('title', 'status', 'pub_date')

admin.site.register(Post)

