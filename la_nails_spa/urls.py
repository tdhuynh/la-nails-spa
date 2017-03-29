from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main.views import HomeView, AboutView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^$', AboutView.as_view(), name='about_view'),
    url(r'^$', ContactView.as_view(), name='contact_view')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
