from django.shortcuts import render
from django.views.generic import CreateView, ListView, ListView, DeleteView, UpdateView
from .forms import CourseForm
from .models import Course
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AddCourse(LoginRequiredMixin, CreateView):
    template_name = 'Courses/course_form.html'
    form_class = CourseForm
    success_url = reverse_lazy('Courses:all_courses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Course'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Course added successfully.')
        return super().form_valid(form)

class AllCourses(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'Courses/all_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all().order_by('-id')

class DeleteCourse(LoginRequiredMixin, DeleteView):
    model = Course
    template_name ='Courses/course_delete.html'
    success_url = reverse_lazy('Courses:all_courses')
    pk_url_kwarg="pk"
    context_object_name = 'course'

    def form_valid(self, form):
        messages.success(self.request, 'Course deleted successfully.')
        return super().form_valid(form)
    

class UpdateCourse(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name ='Courses/course_form.html'
    success_url = reverse_lazy('Courses:all_courses')
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Course'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)