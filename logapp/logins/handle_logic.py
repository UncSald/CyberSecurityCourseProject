from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .models import Log,  Note


def parse_salt(user:User) -> str:
    salt=''
    get_the_spot = 0
    for c in user.password:
        if get_the_spot ==2:
            salt+=c
        if c == '$':
            get_the_spot+=1
    return salt[:-1]



def handle_login(request) -> None:
    # Fix A02:2021 cryptographic failure by hashing
    # hash = PBKDF2PasswordHasher()
    username = request.POST.get('username')
    # Fix A02:2021 cryptographic failure by hashing
    # user_by_username = User.objects.get(username=username)
    # pw = hash.encode(request.POST.get('password'), parse_salt(user_by_username) )
    pw = request.POST.get('password')

    user = User.objects.raw("SELECT * from auth_user WHERE username='%s' AND password='%s'" % (username, pw))[0]
    # Fix A03:2021 injection by adding user input through django built in parameter handling
    # user = User.objects.raw("SELECT * from auth_user WHERE username=%s AND password=%s", [username, pw])[0]
    auth_login(request, user)



def handle_user_creation(request) -> None:
    username = request.POST.get('username')
    pw = request.POST.get('password')
    # Fix A02:2021 cryptographic failure by hashing
    # from django.contrib.auth.hashers import PBKDF2PasswordHasher
    # hash = PBKDF2PasswordHasher()
    # pw = hash.encode(request.POST.get('password'), hash.salt())
    user = User(username=username, password=pw)
    user.save()
    auth_login(request, user)



def handle_log_creation(request) -> None:
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


def return_user_logs(name, user) -> tuple[User, list[Log]]:
    #if User.objects.get(username=name) != user:
    #    raise Exception("no access")
    users = User.objects.get(username=name)
    user_logs = Log.objects.filter(user=users)
    return (users, user_logs)