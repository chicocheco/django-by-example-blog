from django.contrib import admin

from .models import Post


@admin.register(Post)  # admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')  # filter widget
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)  # lookup widget
    date_hierarchy = 'publish'  # display date hierarchy navigation
    ordering = ('status', 'publish')  # order by status, then by publish
