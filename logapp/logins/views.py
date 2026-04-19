from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Log, WorkingTime
from django.contrib.auth.models import User


def front(request):
    if request.user.is_anonymous:
        print('lol', request.user)
        return redirect('login/')
    user_logs = Log.objects.filter(user=request.user)
    return render(request, 'logpage.html', {'logs': user_logs})

def create_log(request):
    if request.method=="GET":
        request.session['timeoflog'] = request.GET.get('timeoflog')
        request.session['login'] = request.GET.get('login')

    return render(request, 'confirm.html')

def confirm_creation(request):
    typeoflog = False
    time = request.session['timeoflog']
    to = request.session['login']
    if to == True:
        typeoflog = True
    new_log = Log(user=request.user, time=time, login=typeoflog)
    new_log.save()
    return redirect('/')

@login_required
def most_hours(request):

    return render(request, 'toplist.html')