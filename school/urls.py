from school.views import DayOfTheWeekListView, DayOfTheWeekDetailView

urlpatterns = [
    path("giorni/", DayOfTheWeekListView.as_view() , name="dayoftheweek"),
    path("giorni/<int:pk>/", DayOfTheWeekDetailView.as_view(), name="dayoftheweek_detail")
]