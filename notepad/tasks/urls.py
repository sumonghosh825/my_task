from django.urls import path
from .views import (
    register, user_login, user_logout, home, 
    task_management, add_task, edit_task, delete_task, 
    profile, update_profile, load_security_content, update_security, 
    load_tasks_by_category,load_tasks_by_status, load_profile_content
)

urlpatterns = [
    # **Authentication Routes**
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]