from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm 
from .  models import Student

# Create your views here.

def student_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form =StudentForm()
        else:
            student=Student.objects.get(pk=id)
            form =StudentForm(instance=student)
        return render(request,'student/form.html',{'form':form})
    else:
        if id==0:
            form =StudentForm(request.POST)
        else:
            student=Student.objects.get(pk=id)
            form =StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')
    
def student_list(request):                                               
             context ={'student_list':Student.objects.all()}	#update it
             return render(request,'student/list.html',context)	#update it
         
def student_delete(request,id):
    student =Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')
   
         








