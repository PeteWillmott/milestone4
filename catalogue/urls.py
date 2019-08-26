from django.conf.urls import url
from .views import view_all, view_one

urlpatterns = [
    url(r'^$', view_all, name="view_all"),
    url(r'^<int:id>', view_one, name="view_one")
]