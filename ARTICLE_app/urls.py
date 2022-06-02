from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home' ),
    path('content/<int:post_id>',views.content,name='content'),
    path('article/<int:post_id>',views.article,name='article'),
    path('weekend/<int:post_id>',views.weekend,name='weekend'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)