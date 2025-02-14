from django.shortcuts import render
from django.views import View
from Teachers.models import Teacher
from Students.models import Student
from Courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def DashboardView(request):
    return render(request, 'Dashboard/dashboard_layout.html')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        stats = [
            {'label': 'Total Teachers', 'value': Teacher.objects.count(), 'icon':'fa-person-chalkboard', 'bg_color': 'bg-green-400'},
            {'label': 'Total Students', 'value': Student.objects.count(), 'icon': 'fa-users', 'bg_color': 'bg-indigo-400'},
            {'label': 'Total Courses', 'value': Course.objects.count(), 'icon': 'fa-book', 'bg_color': 'p-4 bg-red-400'},
        ]
        return render(request, 'Dashboard/dashboard_layout.html', context={
            'stats': stats,
        })
