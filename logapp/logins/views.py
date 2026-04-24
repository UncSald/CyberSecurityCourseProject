from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Log, WorkingTime
from django.contrib.auth.models import User


def front(request):
    if request.user.is_anonymous:
        return redirect('login/')
    return redirect('user/'+str(request.user.username)+'/')

@login_required
def user_view(request, name):
    try:
        users = User.objects.get(username=name)
        if users:
            user_logs = Log.objects.filter(user=users)
            return render(request, 'logpage.html', {'user':name,'logs': user_logs})
    except:
        return redirect('/')

@login_required
def create_log(request):
    if request.method=="GET":
        request.session['timeoflog'] = request.GET.get('timeoflog')
        request.session['login'] = request.GET.get('login')
    return render(request, 'confirm.html')

@login_required
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