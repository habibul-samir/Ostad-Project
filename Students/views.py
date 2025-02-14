from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View
from .forms import StudentForm
from .models import Student
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from Courses.models import Course

# Create your views here.

class AddStudent(LoginRequiredMixin, CreateView):

    form_class = StudentForm
    template_name ='Students/student_form.html'
    success_url = reverse_lazy('Students:all_students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Student'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Student has been added successfully")
        return super().form_valid(form)

class AllStudents(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'Students/all_students.html'
    context_object_name ='students'
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        print(queryset)
        return queryset.order_by('-id')

class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name ='Students/student_delete.html'
    success_url = reverse_lazy('Students:all_students')
    pk_url_kwarg="pk"
    context_object_name = 'student'

    def form_valid(self, form):
        messages.success(self.request, "Student has been deleted successfully")
        return super().form_valid(form)
    

class UpdateStudent(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name ='Students/student_form.html'
    success_url = reverse_lazy('Students:all_students')
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Student has been updated successfully")
        return super().form_valid(form)


class StudentDetails(DetailView):
    model = Student
    template_name ='Students/student_details.html'
    context_object_name ='student'
    pk_url_kwarg = "pk"


class RemoveStudentCourse(View):
    def get(self, request, pk, cid):
        student = Student.objects.get(pk=pk)
        course = Course.objects.get(id=cid)
        student.courses.remove(course)
        messages.success(request, "Course has been removed from student successfully")
        return redirect('Students:student_details', pk=pk)