from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'App/base.html')

#view for the paid stories
def paid(request):
    return render(request,'App/reel.html')

#view for the editor pick
def editor(request):
    return render(request,'App/editor.html')

#view for the adventure stories
def adventure(request):
    return render(request,'App/adven.html')

#view for the short stories
def short(request):
    return render(request,'App/short.html')



#CustomPage after Logout
def logoutview(request):
    return render(request,'registration/logout.html')

#signup forms
def signupview(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            #But if we use form.save() with User Model form only one isssue thw password data will not be encrypte,so for this we have to face problem during login
            #form.save()
            user=form.save()
            user.set_password(user.password)# Here 'set_password' method take care about Hashing Algo for password
            user.save()
            return HttpResponseRedirect('/accounts/login')#If password data of signUpform not encrypteed then login will not work.


    return render(request,'registration/signup.html',{'form':form})
