from django.shortcuts import render,HttpResponseRedirect
from app.models import Student,Admin
from app.forms import StudentForm,AdminForm
from django.db.models import Q
# Create your views here.


def user_dashboard(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect('/')
    obj = Student.objects.all()

    context = {'obj':obj}

    return render(request,'user_dashboard.html',context)


def user_register(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {'form':form}

    return render(request,'user_register.html',context)


def admin_register(request):

    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin_login')

    context = {'form':form}

    return render(request,'admin_register.html',context)


def admin_dashboard(request):
    if not request.session.has_key('email'):
        return HttpResponseRedirect('/admin_login')
    obj = Student.objects.all()

    context = {'obj':obj}

    return render(request,'admin_dashboard.html',context)

def edit_mark(request,stdid):
    ob = Student.objects.get(id=stdid)
    form = StudentForm(instance = ob)
    if request.method == 'POST':

        form = StudentForm(request.POST, request.FILES, instance=ob)
        if form.is_valid():
            print("wwwwwwwwwwwwww")
            form.save()
            return HttpResponseRedirect('/admin_dashboard')
        else:
            print("############INVALID FORM############")
    return render(request,'edit_mark.html',{"form":form},)


def user_login(request):
    login_status=''

    if request.method == 'POST':
        username =  request.POST['username']
        password = request.POST['password1']

        if username is not None and password is not None:
            login = Student.objects.filter(Q(username=username) & Q(password1=password))
            if login:
                request.session['username'] = username
                return HttpResponseRedirect('user_dashboard')

            else:
                login_status = 'Invalid Username or Password'



    context = {"login_status":login_status}
    return render(request,'user_login.html',context)



def admin_login(request):
    login_status=''

    if request.method == 'POST':
        email =  request.POST['email']
        password = request.POST['password1']

        if email is not None and password is not None:
            login = Admin.objects.filter(Q(email=email) & Q(password1=password))
            if login:
                request.session['email'] = email
                return HttpResponseRedirect('admin_dashboard')

            else:
                login_status = 'Invalid Username or Password'



    context = {"login_status":login_status}
    return render(request,'admin_login.html',context)



def admin_logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return HttpResponseRedirect('/admin_login')

def user_logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def edit_profile(request,stdid):
    ob = Student.objects.get(id=stdid)
    form = StudentForm(instance = ob)
    if request.method == 'POST':

        form = StudentForm(request.POST, request.FILES, instance=ob)
        if form.is_valid():
            print("wwwwwwwwwwwwww")
            form.save()
            return HttpResponseRedirect('/user_dashboard')
        else:
            print("############INVALID FORM############")
    return render(request,'edit_profile.html',{"form":form})
