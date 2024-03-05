from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from website import settings
from django.core.mail import send_mail



#@login_required(login_url='login')
def index(request):
    user = request.session.get('user')
    return render(request, 'index.html', {'user': user})
# Create your views here.

def feature(request):
    user=request.session.get('user')
    if request.method=='POST':

        newnotes=notesForm(request.POST, request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
            messages.success(request,"Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'feature.html',{'user':user})

def login(request):
    if request.method =='POST' :
        user=request.POST.get('username')
        pass1=request.POST.get('password')
        try:
            olduser=UserRegister.objects.filter(username=user,password=pass1)
            
            #print(uid.id)
            #print(user,pass1)
        except:
            messages.error(request,'Username Does not Exist!')

        if olduser :
            print(olduser)
            request.session['user']=user   
            return redirect('/')
            messages.success(request,"You have Loged in Successfully")
        else:
           messages.error(request,"username and Password is incorrect!")
    return render(request,'login.html')

def signup(request):
    if request.method =='POST':
        user=request.POST.get('username')
        mobile=request.POST.get('mobile')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        
        if pass1 != pass2:
            messages.error(request,"your password and confirmPassword are not same!")
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            print(newuser.errors)

    return render(request,'signup.html')



def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your feedback has been submitted!")
            messages.success(request,'Your feedback has been submitted!')
            #Email Sending
            sub=request.POST['subject']
            msg=f'Dear User!\n\nThanks for your feedback\nWe will connect shortly!\n\nThank & Regards!\nNotesApp Team\n+91 6351959948 | help@notesapp.com | www.notesapp.com'
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)


            return redirect('/')
        else:
            print(newfeedback.errors)
    return render(request,'contact.html',{'user':user})

def logoutpage(request):
    logout(request)
    messages.error(request,'You have logged out!')
    return redirect('login')

def profilepage(request):
    user=request.session.get('user')
    uid=UserRegister.objects.get(username=user)
    #print(user,uid)
    if request.method=='POST':
        if request.POST.get('profile')=='profile':
            updatereq=updateForm(request.POST,instance=uid)
            if updatereq.is_valid():
                updatereq.save()
                print("Your profile has been updated!")
                messages.success(request, 'Your profile has been updated!')
                return redirect('/profile')
            else:
                print(updatereq.errors)
                messages.error(request,'Your profile could not upadte!')
        

    return render(request,'profile.html',{'user':user,'uid':uid})