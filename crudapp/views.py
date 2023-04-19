from django.shortcuts import render, redirect
from crudapp.forms import studentForm
from crudapp.models import Student


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = studentForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = Student.objects.all()
    return render(request, 'show.html', {'students': students})


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


def update(request, id):
    student = Student.objects.get(id=id)
    form = studentForm(request.POST, instance=Student)
    if form.is_valid():
        form.save()
        return redirect('/show')

    else:
        return render(request, 'edit.html', {'student': student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/show')
