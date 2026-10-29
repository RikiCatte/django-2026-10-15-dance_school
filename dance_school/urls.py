from django.contrib import admin
from django.urls import path, include

from dance_school import views

urlpatterns = [
    # path("", views.test_view, name="test"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
    path("school/", include("schoolmanagement.urls")),
    path("school-conf/", include("school.urls"))
]
