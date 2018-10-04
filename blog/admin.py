from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post


admin.site.site_header = 'Joe Mad Dog - Site Administration'


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Post, PostAdmin)
