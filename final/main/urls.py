from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('contacts', contacts, name="contacts"),
    path('products', products, name="products"),
    path('create/', CreateView.as_view(), name="create"),
    path('login', Login.as_view(), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
