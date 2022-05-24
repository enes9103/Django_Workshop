from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    # print(request.POST) formdaki bilgiler 

    form = StudentForm(request.POST or None)
    if form.is_valid():#backend tarafında formun doğruluğunu kontrol ediyor
        student = form.save()
        if 'profile_pic' in request.FILES:
            student.profile_pic = request.FILES['profile_pic']
            student.save()#media dosyalarını almak için
        # form.clean()
        # return redirect('index')
        messages.success(request, "Student added successful")
        return redirect('student')
        # print(form.cleaned_data.get('first_name'))
    context = {
        'form': form
    }
    return render(request,'student/student.html',context)