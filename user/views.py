from django.shortcuts import render,redirect

from .forms import UserRegistrationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib import messages
from django.contrib.auth import  authenticate,login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request,'user/index.html', {'title':'index'} )


def Register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
         username=form.cleaned_data.get('username')
         email=form.cleaned_data.get('email')

         email_template=get_template('user/Email.html')
         d={'username':username}

         subject,from_email, to='welcome', 'your_email@gmail.com, ', email
         html_content=email_template.render(d)

         msg=EmailMultiAlternatives(subject,from_email, html_content,[to] )
         msg.attatch_alternatives(html_content, "text/html")
         msg.send()

         messages.success(request, f'your acccount has been created successfully ! you are now registerd')
         return redirect('login')
        
    else:
       form=UserRegistrationForm()
           









    return render(request,'user/register.html', {'form':form, 'title':'register here'})
 
# login view 
def Login(request):
    if request.method=='POST':
    #    THIS IS WHAT YOU DO
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, passsword=password)

        if user is not None:

         form=login(request, user)
         messages.success(request, f'welcome {username}')
        else:
           
           messages.info(request, f'account doesnot exist please sign in ')

            


    else:
    #    you return the login form with nothing 
     form =AuthenticationForm()
    
    return render(request, 'login.html', {'form':form}, {'title':'log in'})

    



# Create your views here.
