from django.urls import path

from school.views import DayOfTheWeekListView, DayOfTheWeekDetailView, DayOfTheWeekCreateView, DayOfTheWeekUpdateView

urlpatterns = [
    path("giorni/", DayOfTheWeekListView.as_view() , name="dayoftheweek_list"),
    path("giorni/<int:pk>/", DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail"),
    path("giorni/nuovo/", DayOfTheWeekCreateView.as_view(), name="dayoftheweek_create"),
    path("giorni/<int:pk>/modifica", DayOfTheWeekUpdateView.as_view(), name="dayoftheweek_update")
]