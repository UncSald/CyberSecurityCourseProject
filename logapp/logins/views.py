from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Log, WorkingTime, Note
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


def front(request):
    if request.user.is_anonymous:
        return redirect('login/')
    return redirect('user/'+str(request.user.username)+'/')

@login_required
def user_view(request, name):
    try:
        if name != request.user.username: raise Exception
        users = User.objects.get(username=name)
        user_logs = Log.objects.filter(user=users)
        return render(request, 'logpage.html', {'user':name,'logs': user_logs})
    except:
        return redirect('/')

@login_required
def create_log(request,name):
    if request.method=="GET":
    # Fix csrf:
    # if request.method=="POST":
        request.session['timeoflog'] = request.GET.get('timeoflog')
        request.session['login'] = request.GET.get('login')
        request.session['note'] = request.GET.get('note')
        request.session['user'] = name
        return render(request, 'confirm.html')
    return redirect('/')

@login_required
def confirm_creation(request):
    if request.method=="GET":
    # Fix csrf:
    # if request.method=="POST":
        user = User.objects.get(username=request.session['user'])
        time = request.session['timeoflog']
        log = request.session['login']
        note = request.session['note']
        if note !='':
            new_note = Note(user=user, note_content=note)
            new_note.save()
        new_log = Log(user=user,
                      time=time,
                      login=log,
                      note=new_note if 'new_note' in locals() else None)
        new_log.save()
    return redirect('/')

@login_required
def most_hours(request):
    return render(request, 'toplist.html')