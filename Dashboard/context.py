def dashboard_links(request):

    sidebar_links = [
        {'title': 'Dashboard', 'icon': 'fa-tachometer-alt', 'url': '/dashboard/'},
        {'title': 'Students', 'icon': 'fa-user-graduate', 'url': '/students/'},
        {'title': 'Teachers', 'icon': 'fa-chalkboard-teacher', 'url': '/teachers/'},
        {'title': 'Courses', 'icon': 'fa-book', 'url': '/courses/'},
        # {'title': 'Attendance', 'icon': 'fa-calendar-days', 'url': '/attendance/'},
        # {'title': 'Grades', 'icon': 'fa-graduation-cap', 'url': '/grades/'},
        # {'title': 'Reports', 'icon': 'fa-chart-bar', 'url': '/reports/'},
    ]

    return {
        'sidebar_links': sidebar_links 
    }