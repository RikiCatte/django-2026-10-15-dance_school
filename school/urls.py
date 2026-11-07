from django.urls import path

from school.views import DayOfTheWeekListView, DayOfTheWeekDetailView, DayOfTheWeekCreateView, DayOfTheWeekUpdateView
from school.views import ClassroomListView, ClassroomDetailView, ClassroomCreateView, ClassroomUpdateView
from school.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path("giorni/", DayOfTheWeekListView.as_view() , name="dayoftheweek_list"),
    path("giorni/<int:pk>/", DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path("giorni/nuovo/", DayOfTheWeekCreateView.as_view(), name="dayoftheweek_create"),
    path("giorni/<int:pk>/modifica", DayOfTheWeekUpdateView.as_view(), name="dayoftheweek_update"),

    path("classi/", ClassroomListView.as_view(), name="classroom_list"),
    path("classi/<int:pk>/", ClassroomDetailView.as_view(), name="classroom_detail"),
    path("classi/nuovo/", ClassroomCreateView.as_view(), name="classroom_create"),
    path("classi/<int:pk>/modifica/", ClassroomUpdateView.as_view(), name="classroom_update"),

    path("corsi/", CourseListView.as_view(), name="course_list"),
    path("corsi/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("corsi/nuovo/", CourseCreateView.as_view(), name="course_create"),
    path("corsi/<int:pk>/modifica/", CourseUpdateView.as_view(), name="course_update"),
    path("corsi/<int:pk>/elimina/", CourseDeleteView.as_view(), name="course_delete")

]