from django.shortcuts import render
from .models import *
# Create your views here.
def newSchool(request):
    new = NewsSchool.objects.all().order_by("-time")
    context={
        "new":new
    }
    return render(request, "news.html", context)
