from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User 

# Create your views here.

    

def signup(request):

    if request.method == 'POST':
        Username = request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        date_of_birth = request.POST['date_of_birth']


        myuser = User.object.create_user(username,fname,lname,email,pass1,date_of_birth)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/')


    else:
        return render(request, 'home.html')  