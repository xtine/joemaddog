from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from bio import views as bio_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bio/', bio_views.bio, name='bio'),
    path('blog/', blog_views.blog, name='blog'),
    path('contact/', TemplateView.as_view(template_name='contact.html'),
         name='contact'),
    path('', TemplateView.as_view(template_name='index.html')),
]
