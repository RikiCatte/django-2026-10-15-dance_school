from django.http import HttpResponse
# from django.shortcuts import render

__all__ = []

def test_view(request):
    return HttpResponse(
        "<p>View di prova con HttpResponse</p>"
    )