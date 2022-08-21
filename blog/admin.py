from django.contrib import admin
from blog.models import Post
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')
    prepopulated_fields = {'slug' : ('title',)}

