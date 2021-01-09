from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def home(request):
    return render(request,'enroll/index.html')
def add_data(request):
    
    record = User.objects.all()
    if request.method =="POST":
        obj = StudentRegistration(request.POST)
        if obj.is_valid():
            nm = obj.cleaned_data['name']
            em = obj.cleaned_data['email']
            pw = obj.cleaned_data['password']
            m_obj = User(name=nm,email=em,password=pw)
            m_obj.save()
            return render(request,'enroll/registration.html',{'records':record,'form':obj})
    else:
        obj = StudentRegistration()
        return render(request,'enroll/registration.html',{'form':obj,'records':record})
    
