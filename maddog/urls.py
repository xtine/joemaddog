from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from bio import views as bio_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bio/', bio_views.bio, name='bio'),
    path('blog/', blog_views.blog, name='blog'),
    path('contact/', TemplateView.as_view(template_name='contact.html'),
         name='contact'),
    path('summernote/', include('django_summernote.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
