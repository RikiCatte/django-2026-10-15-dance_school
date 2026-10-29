from django.views import generic

from school.models import DayOfTheWeek

__all__ = ["DayOfTheWeekListView", "DayOfTheWeekDetailView"]

class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek

class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek