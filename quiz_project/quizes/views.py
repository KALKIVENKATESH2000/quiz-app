from typing import Optional
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Exam
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            if request.POST['usertype']=='teacher':
                user.is_staff=True
                user.save()
            else:
                user.is_staff=False
                user.save()
            login(request, user)
            return redirect('signup')
        messages.error(request, "Unsuccessful registration. invalid information.")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



def signup(request):
	if request.method == "POST":
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request,"valid username or password.")
				if user.is_staff==True:
					return redirect('teacher')
			
				else:
					return redirect('student')
				
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", {"login_form":form})

def logout_view(request):
	logout(request)
	messages.info(request, f'You have successfully logout')
	return redirect('register')

def teacher(request):
    questions=Exam.objects.all()
    return render(request, 'teacher.html', {'questions':questions})

def add(request):
    if request.method=="GET":
        return render(request,'addquestions.html')
    else:
        Exam (
            question=request.POST.get('quest'),
            option1=request.POST.get('op1'),
            option2=request.POST.get('op2'),
            option3=request.POST.get('op3'),
            option4=request.POST.get('op4'),
            carrans=request.POST.get('ans')
        ).save()
        return redirect('teacher')


def student(request):
    return render(request, 'student.html')


def update(request,id):
    if request.method=="GET":
        updatequestion=Exam.objects.get(id=id)
        return render(request,'update.html',{'updatequestion':updatequestion})
    else:
        updatequestion=Exam.objects.get(id=id)
        updatequestion.question=request.POST['quest']
        updatequestion.option1=request.POST['op1']
        updatequestion.option2=request.POST['op2']
        updatequestion.option3=request.POST['op3']
        updatequestion.option4=request.POST['op4']
        updatequestion.carrans=request.POST['ans']

        updatequestion.save()
        return redirect('teacher')

def deletequestion(request,id):
	delquestion=Exam.objects.get(id=id)
	delquestion.delete()
	return redirect('teacher')

def examonline(request):
    result=Exam.objects.all()
    return render(request, 'base.html',{"Exam":result})

