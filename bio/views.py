from django.http import HttpResponseRedirect
from django.shortcuts import render


def bio(request):
    return render(request, 'bio.html')
