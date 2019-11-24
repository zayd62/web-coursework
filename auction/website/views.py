from django.shortcuts import render
from django.http import Http404
from django.db import IntegrityError
from website import models
from django.contrib.auth.models import User
import datetime
# Create your views here.
appname = 'notEbay'


def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try:
                user = User.objects.get(username=username)
            except models.Profile.user.DoesNotExist:
                raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request, 'mainapp/not-logged-in.html', {})
    return mod_view

# bobobobo123
def index(request):
    context = {'appname': appname}
    return render(request, 'website/index.html', context)


def signup(request):
    context = {'appname': appname}
    return render(request, 'website/signup.html', context)


def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']
        dob_dateobj = datetime.date.fromisoformat(str(dob))

        user = User()
        user.username = u
        user.set_password(p)
        user.email = email

        profile = models.Profile()
        profile.birth_date = dob_dateobj
        profile.user = user

        try:
            user.save()
        except IntegrityError:
            raise Http404(
                'Username '+u+' already taken: Usernames must be unique')
        try:
            profile.save()
        except Exception as e:
            print(e)
        context = {
            'appname': appname,
            'username': u
        }
        return render(request, 'website/index.html', context)

    else:
        raise Http404('POST data missing')


def login(request):
    if not ('username' in request.POST and 'password' in request.POST):
        context = {'appname': appname}
        return render(request, 'website/login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try:
            member = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404('User does not exist')
        if member.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
                'appname': appname,
                'username': username,
                'loggedin': True
            }
            response = render(request, 'website/index.html', context)

            # remember last login in cookie
            now = datetime.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  # one year
            delta = now + datetime.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = datetime.datetime.strftime(delta, format)
            response.set_cookie('last_login', now, expires=expires)
            return response
        else:
            raise Http404('Wrong password')


@loggedin
def logout(request, user):
    request.session.flush()
    context = {'appname': appname}
    return render(request, 'website/index.html', context)
