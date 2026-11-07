from django.urls import reverse_lazy
from django.views import generic

from school.models import Classroom, Course, DayOfTheWeek

__all__ = [
    "DayOfTheWeekListView",
    "DayOfTheWeekDetailView",
    "DayOfTheWeekCreateView",
    "DayOfTheWeekUpdateView",
    "ClassroomListView",
    "ClassroomDetailView",
    "ClassroomUpdateView",
    "ClassroomCreateView",
    "CourseListView",
    "CourseDetailView",
    "CourseCreateView",
    "CourseUpdateView",
    "CourseDeleteView",
]


class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek


# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# @method_decorator(login_required, name="dispatch")
class DayOfTheWeekCreateView(generic.CreateView):
    model = DayOfTheWeek
    fields = ["name", "number"]
    success_url = reverse_lazy("dayoftheweek_list")


class DayOfTheWeekUpdateView(generic.UpdateView):
    model = DayOfTheWeek
    fields = ["name", "number"]

    def get_success_url(self):
        return reverse_lazy("dayoftheweek_detail", kwargs={"pk": self.object.pk})


class ClassroomListView(generic.ListView):
    model = Classroom


class ClassroomDetailView(generic.DetailView):
    model = Classroom


class ClassroomCreateView(generic.CreateView):
    model = Classroom
    fields = ["name", "capacity"]
    success_url = reverse_lazy("classroom_list")


class ClassroomUpdateView(generic.UpdateView):
    model = Classroom
    fields = ["name", "capacity"]

    def get_success_url(self):
        return reverse_lazy("classroom_detail", kwargs={"pk": self.object.pk})


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course


class CourseCreateView(generic.CreateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseUpdateView(generic.UpdateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy("course_list")
