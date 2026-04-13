from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Log, WorkingTime
from django.contrib.auth.models import User


@login_required
def index(request):
    user_logs = Log.objects.filter(user=request.user)
    return render(request, 'logpage.html', {'logs': user_logs})

