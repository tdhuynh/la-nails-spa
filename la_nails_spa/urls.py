from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main.views import IndexView, AboutView, ContactView, ServicesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^about$', AboutView.as_view(), name='about_view'),
    url(r'^contact$', ContactView.as_view(), name='contact_view'),
    url(r'^services$', ServicesView.as_view(), name='services_view')
]
