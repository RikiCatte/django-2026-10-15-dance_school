from django.urls import path

from school.views import DayOfTheWeekListView, DayOfTheWeekDetailView

urlpatterns = [
    path("giorni/", DayOfTheWeekListView.as_view() , name="dayoftheweek_list"),
    path("giorni/<int:pk>/", DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail")
]