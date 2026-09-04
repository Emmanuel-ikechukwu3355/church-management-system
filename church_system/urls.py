from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard
    path('', include('dashboard.urls')),

    # Members
    path('members/', include('members.urls')),

    # Attendance
    path('attendance/', include('attendance.urls')),

    # Events
    path('events/', include('events.urls')),
]