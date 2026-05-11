from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .handle_logic import handle_login, handle_user_creation, handle_log_creation, return_user_logs, check_user_auth

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        try:
            handle_login(request)
        except Exception as e:
            print(e)
            return redirect('/')
    return redirect('/')

def create_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')
    if request.method == 'POST':
        handle_user_creation(request)
    return redirect('/')

def front(request):
    if request.user.is_anonymous:
        return redirect('login/')
    return redirect('user/'+str(request.user.username)+'/')

@login_required
def user_view(request, name):
    try:
        # check_user_auth(name,request.user)
        users, user_logs = return_user_logs(name)
        return render(request, 'logpage.html', {'user':users,'logs': user_logs})
    except Exception:
        return redirect('/')

@login_required
def create_log(request,name):
    if request.method=="GET":
    # Fix csrf vulnerability:
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
    # Fix csrf vulnerability:
    # if request.method=="POST":
        handle_log_creation(request)
    return redirect('/')

def csrf(request):
    return render(request, 'csrf.html')