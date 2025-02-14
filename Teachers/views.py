from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import TeacherForm
from .models import Teacher
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AddTeacher(LoginRequiredMixin, CreateView):
    template_name = 'Teachers/teacher_form.html'
    form_class = TeacherForm
    success_url = reverse_lazy("Teachers:all_teachers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Teacher'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Teacher added successfully.')
        return super().form_valid(form)
    
class AllTeachers(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'Teachers/all_teachers.html'
    context_object_name ='teachers'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')


class UpdateTeacher(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name ='Teachers/teacher_form.html'
    success_url = reverse_lazy("Teachers:all_teachers")
    pk_url_kwarg="pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Teacher'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Teacher updated successfully.')
        return super().form_valid(form)

class DeleteTeacher(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name ='Teachers/teacher_delete.html'
    success_url = reverse_lazy("Teachers:all_teachers")
    pk_url_kwarg="pk"

    def form_valid(self, form):
        messages.success(self.request, 'Teacher Deleted successfully.')
        return super().form_valid(form)