from django.shortcuts import render, redirect
from django.contrib import messages 
from .models.students import Students
from .forms import StudentForm

# Create your views here.
def homepage(request):
  return render(request, 'homepage/index.html')

def about(request):
  return render(request, 'homepage/about.html')

def student_index(request):
    students = Students.objects.all()
    return render(request, 'student/index.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mahasiswa berhasil dibuat!')
            return redirect('student_index')
    else:
        form = StudentForm()
    return render(request, 'student/create.html', {'form': form})
