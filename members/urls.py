# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.member_list, name='member_list'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member, name='add_member'),
    path('edit/<int:id>/', views.edit_member, name='edit_member'),
    path('delete/<int:id>/', views.delete_member, name='delete_member'),
    path('dashboard/', views.dashboard, name='dashboard'),
]