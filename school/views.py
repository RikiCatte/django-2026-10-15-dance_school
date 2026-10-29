from django.urls import reverse_lazy
from django.views import generic

from school.models import DayOfTheWeek

__all__ = ["DayOfTheWeekListView", "DayOfTheWeekDetailView", "DayOfTheWeekCreateView"]

class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek

class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek

class DayOfTheWeekCreateView(generic.CreateView):
    model = DayOfTheWeek
    fields = ["name", "number"]
    success_url = reverse_lazy("dayoftheweek_list")

class DayOfTheWeekUpdateView(generic.UpdateView):
    model = DayOfTheWeek
    fields = ["name", "number"]
    
    def get_success_url(self):
        return reverse_lazy(
            "dayoftheweek_detail",
            kwargs={ "pk": self.object.pk }
        )