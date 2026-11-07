# from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

__all__ = ["home", "about", "api_example"]

# def test_view(request):
#     return HttpResponse(
#         "<p>View di prova con HttpResponse</p>"
#     )


def home(request):
    context = {
        "testo": "Benvenuti! Scopri i nostri corsi e iscriviti alla stagione 2026/2027.",
    }
    return render(
        request,
        template_name="home.html",
        context=context,
    )


def about(request):
    return render(request, template_name="about.html")


def api_example(request):
    data = {"name": "Ciao", "email": "ciao@ciao.it"}

    return JsonResponse(data)
