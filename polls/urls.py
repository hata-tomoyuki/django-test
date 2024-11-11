from django.conf import settings
from django.urls import include, path

from . import views

# 名前空間
app_name = "polls"
# 各URL
urlpatterns = [
    path("", views.index, name="index"),
]
